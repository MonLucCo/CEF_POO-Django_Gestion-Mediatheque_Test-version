from django import forms
from django.http.request import MediaType

from bibliothecaire.models import Media, Livre, Dvd, Cd


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
