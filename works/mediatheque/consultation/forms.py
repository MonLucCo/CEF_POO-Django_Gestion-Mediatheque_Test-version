from django import forms


class SupportFilterForm(forms.Form):
    TYPE_CHOICES = [
        ('all', 'Tous les supports consultables'),
        ('medias', 'Médias consultables'),
        ('jeux', 'Jeux de plateau consultables'),
        ('disponibles', 'Médias disponibles à l’emprunt'),
        ('vide', 'Test liste vide'),
    ]
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, label="Filtrer par")
