from django import forms
from django.db.models import Case, When, IntegerField

from bibliothecaire.models import Media, Livre, Dvd, Cd, Membre, Emprunt, StatutEmprunt


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = [
            'name',
            'annee_edition',
            'theme',
            'media_type',    # media_type est exposé selon 'is_update'
            # consultable et disponible sont fixés dans la vue
        ]
        labels = {
            'name':'Titre du média',
            'annee_edition':"Année d'édition",
            'theme':'Thématique',
            'media_type' : 'Type de média',
        }

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super(MediaForm, self).__init__(*args, **kwargs)

        if is_update != True:
            self.fields.pop('media_type', None)


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = [
            'name',
            'annee_edition',
            'theme',
            'auteur',
            'nb_page',
            'resume',
            'consultable',
            # disponible est fixé dans la vue
            # media_type est fixé dans la vue
        ]


class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = [
            'name',
            'annee_edition',
            'theme',
            'realisateur',
            'duree',
            'histoire',
            'consultable',
            # disponible est fixé dans la vue
            # media_type est fixé dans la vue
        ]


class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = [
            'name',
            'annee_edition',
            'theme',
            'artiste',
            'nb_piste',
            'duree_ecoute',
            'consultable',
            # disponible est fixé dans la vue
            # media_type est fixé dans la vue
        ]


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ["name"]  # uniquement les champs saisissables
        labels = {'name':'Nom du Membre'}


class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ["emprunteur", "media"]
        labels = {
            "emprunteur": "Membre emprunteur",
            "media": "Média à emprunter",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tri des membres : nom puis compte
        self.fields["emprunteur"].queryset = Membre.objects.order_by("name", "compte")

        # Tri métier des médias : nom puis type (CD > DVD > LIVRE > NON_DEFINI)
        media_queryset = Media.objects.annotate(
            type_priority=Case(
                When(media_type='CD', then=4),
                When(media_type='DVD', then=3),
                When(media_type='LIVRE', then=2),
                When(media_type='NON_DEFINI', then=1),
                default=0,
                output_field=IntegerField()
            )
        ).order_by("name", "-type_priority")

        self.fields["media"].queryset = media_queryset


class EmpruntRendreForm(forms.Form):
    emprunt = forms.ModelChoiceField(
        queryset=Emprunt.objects.exclude(statut=StatutEmprunt.RENDU),
        label="Emprunt à rendre"
    )

    media = forms.ModelChoiceField(
        queryset=Media.objects.filter(disponible=False),
        label="Média emprunté",
        required=False,
        disabled=True
    )

    emprunteur = forms.ModelChoiceField(
        queryset=Membre.objects.filter(emprunts__statut__in=[StatutEmprunt.EN_COURS, StatutEmprunt.RETARD]).distinct(),
        label="Membre emprunteur",
        required=False,
        disabled=True
    )


class EmpruntRetourForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = []  # Aucun champ modifiable
