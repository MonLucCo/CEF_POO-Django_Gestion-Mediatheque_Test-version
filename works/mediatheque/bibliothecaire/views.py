from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Media

# Create your views here.

# accueil
class AccueilBibliothecaireView(TemplateView):
    template_name = 'bibliothecaire/accueil.html'
# Media
class MediaListView(ListView):
    model = Media
    context_object_name = 'medias'
    template_name = 'bibliothecaire/medias/media_list.html'
class MediaDetailView(DetailView):
    model = Media
    context_object_name = 'media'
    template_name = 'bibliothecaire/medias/media_detail.html'

    def get_object(self, queryset=None):
        obj = super(MediaDetailView, self).get_object(queryset)
        return obj.get_real_instance()
