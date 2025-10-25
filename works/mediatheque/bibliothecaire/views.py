from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView

from bibliothecaire.models import Media, Livre, Dvd, Cd, Membre, StatutMembre
from bibliothecaire.forms import MediaForm, LivreForm, DvdForm, CdForm
from django.db import transaction


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

    def get_context_data(self, **kwargs):
        context = super(MediaCreateView, self).get_context_data(**kwargs)
        context['is_non_defini'] = True
        # context['is_typage'] = False
        return context

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
        # context['is_typage'] = False
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
        # context['is_typage'] = False
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
        # context['is_typage'] = False
        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False     # Champ exposé dans la vue
        form.instance.disponible = True         # Selon valeur de 'consultable', Etat1 pour false ou Etat3 pour True
        form.instance.media_type = 'CD'

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(MediaCdCreateView, self).form_valid(form)


class MediaUpdateView(UpdateView):
    model = Media
    form_class = MediaForm
    template_name = 'bibliothecaire/medias/media_form.html'

    # 1. Sauvegarde du type initial pour comparaison
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.old_media_type = obj.media_type
        return obj

    # 2. Comparaison dy type initial avec le type du formulaire (savoir s'il s'agit d'un changement de type)
    def is_typage_transition(self, form):
        old_type = self.old_media_type
        new_type = form.cleaned_data.get('media_type')
        return old_type == 'NON_DEFINI' and new_type != 'NON_DEFINI'

    # 3. Transmission du paramètre is_update au formulaire
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = True
        return kwargs

    # 4. Ajout de variables au contexte pour affichage conditionnel dans le template
    def get_context_data(self, **kwargs):
        context = super(MediaUpdateView, self).get_context_data(**kwargs)
        context['is_update'] = True

        for key, _ in Media.TYPE_CHOICES:
            context[f'is_{key.lower()}'] = self.object.media_type == key

        return context

    # 5. Logique fonctionnelle : mise à jour spécifique au cycle de vie fonctionnel
    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False         # Valeur par défaut dans le modèle
        # form.instance.disponible = False          # Valeur par défaut dans le modèle
        # form.instance.media_type = 'NON_DEFINI'   # Valeur par défaut dans le modèle
        pass

    # 6. Logique métier : mise à jour ou redirection selon changement de type
    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        is_typage = self.is_typage_transition(form)

        # Cas : media_type modifié vers un type réel → redirection vers création typée
        if is_typage:
            media = form.save(commit=False)     # contient les données du formulaire nettoyées et sans sauvegarde
            return redirect(media.get_typage_url_name(), pk=media.pk)

        # Cas classique : mise à jour sans changement de type
        return super(MediaUpdateView, self).form_valid(form)

    # 7. Redirection après succès
    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class LivreUpdateView(UpdateView):
    model = Livre
    form_class = LivreForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_context_data(self, **kwargs):
        context = super(LivreUpdateView, self).get_context_data(**kwargs)
        context['is_update'] = True
        context['is_livre'] = True

        # media = Media.objects.get(pk=self.object.pk)
        # context['is_typage'] = media.is_typage_incomplete()

        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False         # Champ exposé dans la vue
        # form.instance.disponible = True           # Selon valeur de 'consultable', Etat1 pour False ou Etat3 pour True
        # form.instance.media_type = 'LIVRE'        # Champ figé (non exposé) dans la vue
        pass

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(LivreUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class DvdUpdateView(UpdateView):
    model = Dvd
    form_class = DvdForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_context_data(self, **kwargs):
        context = super(DvdUpdateView, self).get_context_data(**kwargs)
        context['is_update'] = True
        context['is_dvd'] = True

        # media = Media.objects.get(pk=self.object.pk)
        # context['is_typage'] = media.is_typage_incomplete()

        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False         # Champ exposé dans la vue
        # form.instance.disponible = True           # Selon valeur de 'consultable', Etat1 pour False ou Etat3 pour True
        # form.instance.media_type = 'DVD'        # Champ figé (non exposé) dans la vue
        pass

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(DvdUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class CdUpdateView(UpdateView):
    model = Cd
    form_class = CdForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_context_data(self, **kwargs):
        context = super(CdUpdateView, self).get_context_data(**kwargs)
        context['is_update'] = True
        context['is_cd'] = True

        # media = Media.objects.get(pk=self.object.pk)
        # context['is_typage'] = media.is_typage_incomplete()

        return context

    def set_lifecycle_flags(self, form):
        # form.instance.consultable = False         # Champ exposé dans la vue
        # form.instance.disponible = True           # Selon valeur de 'consultable', Etat1 pour False ou Etat3 pour True
        # form.instance.media_type = 'CD'        # Champ figé (non exposé) dans la vue
        pass

    def form_valid(self, form):
        self.set_lifecycle_flags(form)
        return super(CdUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class MediaCancelTypingView(View):
    def post(self, request, pk):
        media = get_object_or_404(Media, pk=pk)

        if media.media_type == 'LIVRE':
            Livre.objects.filter(pk=pk).delete()
        elif media.media_type == 'DVD':
            Dvd.objects.filter(pk=pk).delete()
        elif media.media_type == 'CD':
            Cd.objects.filter(pk=pk).delete()

        media.media_type = 'NON_DEFINI'
        media.save()

        return redirect('bibliothecaire:media_list')


class MediaTypageLivreView(FormView):
    form_class = LivreForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_object(self):
        return get_object_or_404(Media, pk=self.kwargs['pk'])

    def get_initial(self):
        media = self.get_object()
        return {
            'name': media.name,
            'annee_edition': media.annee_edition,
            'theme': media.theme,
            'consultable': media.consultable,
            'disponible': True,                 # Valeur (facultative) indiquée pour la compréhension, mais non exposée
            'media_type': 'LIVRE',              # Valeur (facultative) indiquée pour la compréhension, mais non exposée
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_typage'] = True
        context['is_livre'] = True
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        media = self.get_object()

        with transaction.atomic():
            # Mise à jour du media_type dans Media
            media.media_type = 'LIVRE'
            media.save()

            # Création ou récupération du sous-type
            typed_instance = media.mutate_to_typed()

            # Application des champs spécifiques du formulaire
            for field in typed_instance.get_specific_fields():
                setattr(typed_instance, field, form.cleaned_data.get(field))

            typed_instance.save()

        return super(MediaTypageLivreView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class MediaTypageDvdView(FormView):
    form_class = DvdForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_object(self):
        return get_object_or_404(Media, pk=self.kwargs['pk'])

    def get_initial(self):
        media = self.get_object()
        return {
            'name': media.name,
            'annee_edition': media.annee_edition,
            'theme': media.theme,
            'consultable': media.consultable,
            'disponible': True,                  # Valeur (facultative) indiquée pour la compréhension, mais non exposée
            'media_type': 'DVD',                 # Valeur (facultative) indiquée pour la compréhension, mais non exposée
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_typage'] = True
        context['is_dvd'] = True
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        media = self.get_object()

        with transaction.atomic():
            # Mise à jour du media_type dans Media
            media.media_type = 'DVD'
            media.save()

            # Création ou récupération du sous-type
            typed_instance = media.mutate_to_typed()

            # Application des champs spécifiques du formulaire
            for field in typed_instance.get_specific_fields():
                setattr(typed_instance, field, form.cleaned_data.get(field))

            typed_instance.save()

        return super(MediaTypageDvdView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class MediaTypageCdView(FormView):
    form_class = CdForm
    template_name = 'bibliothecaire/medias/media_form.html'

    def get_object(self):
        return get_object_or_404(Media, pk=self.kwargs['pk'])

    def get_initial(self):
        media = self.get_object()
        return {
            'name': media.name,
            'annee_edition': media.annee_edition,
            'theme': media.theme,
            'consultable': media.consultable,
            'disponible': True,                  # Valeur (facultative) indiquée pour la compréhension, mais non exposée
            'media_type': 'CD',                  # Valeur (facultative) indiquée pour la compréhension, mais non exposée
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_typage'] = True
        context['is_cd'] = True
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        media = self.get_object()

        with transaction.atomic():
            # Mise à jour du media_type dans Media
            media.media_type = 'CD'
            media.save()

            # Création ou récupération du sous-type
            typed_instance = media.mutate_to_typed()

            # Application des champs spécifiques du formulaire
            for field in typed_instance.get_specific_fields():
                setattr(typed_instance, field, form.cleaned_data.get(field))

            typed_instance.save()

        return super(MediaTypageCdView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bibliothecaire:media_list')


class MembreListView(ListView):
    model = Membre
    context_object_name = 'membres'
    template_name = 'bibliothecaire/membres/membre_list.html'


class MembreEnGestionView(MembreListView):
    def get_queryset(self):
        return Membre.objects.exclude(statut=StatutMembre.ARCHIVE).order_by("name")


class MembreEmprunteursView(MembreListView):
    def get_queryset(self):
        return Membre.objects.filter(statut=StatutMembre.EMPRUNTEUR).order_by("name")


class MembreArchivesView(MembreListView):
    def get_queryset(self):
        return Membre.objects.filter(statut=StatutMembre.ARCHIVE).order_by("name")
