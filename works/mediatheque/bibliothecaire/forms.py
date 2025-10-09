from django import forms
from bibliothecaire.models import Media, Livre, Dvd, Cd


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = [
            'name',
            'annee_edition',
            'theme'
            # consultable, disponible et media_type sont fixés dans la vue
        ]
        labels = {
            'name':'Titre du média',
            'annee_edition':"Année d'édition",
            'theme':'Thématique',
        }


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
