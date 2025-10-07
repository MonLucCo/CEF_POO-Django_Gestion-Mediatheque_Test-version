from django import forms
from bibliothecaire.models import Media

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

