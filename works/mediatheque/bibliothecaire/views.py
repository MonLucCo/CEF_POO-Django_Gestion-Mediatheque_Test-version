from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from bibliothecaire.models import Media
from bibliothecaire.forms import MediaForm, LivreForm, DvdForm, CdForm


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


class MediaNonTypeListView(MediaListByTypeView):
    def get_queryset(self):
        return Media.objects.filter(media_type='NON_DEFINI')


class MediaCreateView(CreateView):
    model = Media
    form_class = MediaForm
    template_name = 'bibliothecaire/medias/media_form.html'
    success_url = reverse_lazy('bibliothecaire:media_list')

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False         # Valeur par défaut dans le modèle
        # form.instance.disponible = False          # Valeur par défaut dans le modèle
        # form.instance.media_type = 'NON_DEFINI'   # Valeur par défaut dans le modèle
        pass

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(MediaCreateView, self).form_valid(form)


class MediaLivreCreateView(MediaCreateView):
    form_class = LivreForm

    def get_context_data(self, **kwargs):
        context = super(MediaLivreCreateView, self).get_context_data(**kwargs)
        context['is_livre'] = True
        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False     # Champ exposé dans la vue
        form.instance.disponible = True         # Selon valeur de 'consultable', Etat1 pour false ou Etat3 pour True
        form.instance.media_type = 'LIVRE'

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(MediaLivreCreateView, self).form_valid(form)


class MediaDvdCreateView(MediaCreateView):
    form_class = DvdForm

    def get_context_data(self, **kwargs):
        context = super(MediaDvdCreateView, self).get_context_data(**kwargs)
        context['is_dvd'] = True
        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False     # Champ exposé dans la vue
        form.instance.disponible = True         # Selon valeur de 'consultable', Etat1 pour false ou Etat3 pour True
        form.instance.media_type = 'DVD'

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(MediaDvdCreateView, self).form_valid(form)


class MediaCdCreateView(MediaCreateView):
    form_class = CdForm

    def get_context_data(self, **kwargs):
        context = super(MediaCdCreateView, self).get_context_data(**kwargs)
        context['is_cd'] = True
        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False     # Champ exposé dans la vue
        form.instance.disponible = True         # Selon valeur de 'consultable', Etat1 pour false ou Etat3 pour True
        form.instance.media_type = 'CD'

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(MediaCdCreateView, self).form_valid(form)
