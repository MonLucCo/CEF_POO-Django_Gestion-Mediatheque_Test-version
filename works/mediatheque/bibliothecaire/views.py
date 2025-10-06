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
class MediaListConsultableView(MediaListView):
    def get_queryset(self):
        return Media.objects.filter(consultable=True)
    def get_context_data(self, **kwargs):
        context = super(MediaListConsultableView, self).get_context_data(**kwargs)
        context['filtrage'] = 'consultables'
        context['consultable'] = True
        return context
class MediaListDisponibleView(MediaListView):
    def get_queryset(self):
        return Media.objects.filter(consultable=True, disponible=True)
    def get_context_data(self, **kwargs):
        context = super(MediaListDisponibleView, self).get_context_data(**kwargs)
        context['filtrage'] = 'disponibles'
        context['disponible'] = True
        return context


class MediaListByTypeView(MediaListView):
    def get_queryset(self):
        rqt_media_type = self.request.GET.get('type')
        if rqt_media_type in ['LIVRE', 'DVD', 'CD']:
            return Media.objects.filter(media_type=rqt_media_type)
        return Media.objects.none()

    def get_context_data(self, **kwargs):
        context = super(MediaListByTypeView, self).get_context_data(**kwargs)
        rqt_media_type = self.request.GET.get('type')
        context['filtrage'] = f"type: {rqt_media_type}" if rqt_media_type else "type inconnu"
        context['media_type'] = rqt_media_type
        return context