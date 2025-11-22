from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from consultation.forms import SupportFilterForm
from bibliothecaire.models import Media, JeuDePlateau


# Create your views here.

# accueil
class AccueilConsultationView(TemplateView):
    template_name = 'consultation/accueil.html'


# consultation supports
class SupportListView(FormView):
    form_class = SupportFilterForm
    template_name = 'consultation/supports/supports_list.html'

    def form_valid(self, form):
        filtre = form.cleaned_data['type']
        if filtre == 'medias':
            return redirect('consultation:supports_medias')
        elif filtre == 'jeux':
            return redirect('consultation:supports_jeux')
        elif filtre == 'disponibles':
            return redirect('consultation:supports_medias_disponibles')
        elif filtre == 'vide':
            return redirect('consultation:supports_vide')
        else:
            return redirect('consultation:supports')

    def get(self, request, *args, **kwargs):
        route_name = request.resolver_match.url_name
        filtre = {
            'supports_medias': 'medias',
            'supports_jeux': 'jeux',
            'supports_medias_disponibles': 'disponibles',
            'supports': 'all',
            'supports_vide': 'vide'
        }.get(route_name, 'all')

        form = self.form_class(initial={'type':filtre})

        if filtre == 'medias':
            supports = Media.objects.filter(consultable=True)
        elif filtre == 'jeux':
            supports = JeuDePlateau.objects.filter(consultable=True)
        elif filtre == 'disponibles':
            supports = Media.objects.filter(consultable=True, disponible=True)
        elif filtre == 'all':
            supports = list(Media.objects.filter(consultable=True)) + list(JeuDePlateau.objects.filter(consultable=True))
        else:
            supports = None

        return self.render_to_response(self.get_context_data(form=form, supports=supports))
