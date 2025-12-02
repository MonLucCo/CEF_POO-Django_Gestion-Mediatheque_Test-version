from django.urls import path
from . import views
from .decorator import bibliothecaire_required
from .views import EmpruntCreateFromMembreView, EmpruntCreateFromMediaView, EmpruntRendreView, EmpruntRetourConfirmView, \
    EmpruntRendreFromMediaView, EmpruntRendreFromMembreView
from .views_debug import ResetRetardSessionView

app_name = 'bibliothecaire'

urlpatterns = [
    # Accueil
    path('', bibliothecaire_required(views.AccueilBibliothecaireView.as_view()), name='accueil'),
    path('accueil/', bibliothecaire_required(views.AccueilBibliothecaireView.as_view()), name='accueil'),

    # Media (Livre, Dvd, Cd)
    # Listes
    path('medias/', bibliothecaire_required(views.MediaListView.as_view()), name='media_list'),
    path('medias/consultables/', bibliothecaire_required(views.MediaListConsultableView.as_view()), name='media_list_consultables'),
    path('medias/disponibles/', bibliothecaire_required(views.MediaListDisponibleView.as_view()), name='media_list_disponibles'),
    path('medias/types/', bibliothecaire_required(views.MediaListByTypeView.as_view()), name='media_list_by_type'),
    path('medias/non-types/', bibliothecaire_required(views.MediaNonTypeListView.as_view()), name='media_list_non_types'),
    # Détails
    path('medias/<int:pk>/', bibliothecaire_required(views.MediaDetailView.as_view()), name='media_detail'),
    # Création
    path('medias/ajouter/', bibliothecaire_required(views.MediaCreateView.as_view()), name='media_create'),
    path('medias/ajouter/livre', bibliothecaire_required(views.MediaLivreCreateView.as_view()), name='media_create_livre'),
    path('medias/ajouter/dvd', bibliothecaire_required(views.MediaDvdCreateView.as_view()), name='media_create_dvd'),
    path('medias/ajouter/cd', bibliothecaire_required(views.MediaCdCreateView.as_view()), name='media_create_cd'),
    # Mise à jour
    path('medias/<int:pk>/modifier/', bibliothecaire_required(views.MediaUpdateView.as_view()), name='media_update'),
    path('medias/<int:pk>/modifier/livre/', bibliothecaire_required(views.MediaTypageLivreView.as_view()), name='media_typage_livre'),
    path('medias/<int:pk>/modifier/dvd/', bibliothecaire_required(views.MediaTypageDvdView.as_view()), name='media_typage_dvd'),
    path('medias/<int:pk>/modifier/cd/', bibliothecaire_required(views.MediaTypageCdView.as_view()), name='media_typage_cd'),

    path("medias/<int:pk>/emprunter", bibliothecaire_required(EmpruntCreateFromMediaView.as_view()), name="media_emprunter"),
    path("medias/<int:pk>/rendre/", bibliothecaire_required(EmpruntRendreFromMediaView.as_view()), name="media_rendre"),

    path('medias/<int:pk>/livre/modifier/', bibliothecaire_required(views.LivreUpdateView.as_view()), name='media_update_livre'),
    path('medias/<int:pk>/dvd/modifier/', bibliothecaire_required(views.DvdUpdateView.as_view()), name='media_update_dvd'),
    path('medias/<int:pk>/cd/modifier/', bibliothecaire_required(views.CdUpdateView.as_view()), name='media_update_cd'),

    path('medias/<int:pk>/annuler_typage/', bibliothecaire_required(views.MediaCancelTypingView.as_view()), name='media_cancel_typing'),

    # Emprunts
    path('emprunts/', bibliothecaire_required(views.EmpruntListView.as_view()), name='emprunt_list'),
    path('emprunts/retards/', bibliothecaire_required(views.EmpruntRetardView.as_view()), name='emprunt_retard'),
    path('emprunts/ajouter/', bibliothecaire_required(views.EmpruntCreateView.as_view()), name='emprunt_create'),
    path("emprunts/rendre/", bibliothecaire_required(EmpruntRendreView.as_view()), name="emprunt_rendre"),
    path("emprunts/<int:pk>/retour/confirmation/", bibliothecaire_required(EmpruntRetourConfirmView.as_view()), name="emprunt_retour_confirm"),

    # Membres
    path('membres/', bibliothecaire_required(views.MembreListView.as_view()), name='membre_list'),
    path('membres/liste', bibliothecaire_required(views.MembreEnGestionView.as_view()), name='membre_list_gestion'),
    path('membres/liste/emprunteurs', bibliothecaire_required(views.MembreEmprunteursView.as_view()), name='membre_list_emprunteurs'),
    path('membres/liste/supprimes', bibliothecaire_required(views.MembreArchivesView.as_view()), name='membre_list_archives'),
    path('membres/ajouter/', bibliothecaire_required(views.MembreCreateView.as_view()), name='membre_create'),
    path('membres/ajouter/emprunteur', bibliothecaire_required(views.MembreCreateEmprunteurView.as_view()), name='membre_create_emprunteur'),
    path('membres/<int:pk>/', bibliothecaire_required(views.MembreDetailView.as_view()), name='membre_detail'),
    path('membres/<int:pk>/modifier/', bibliothecaire_required(views.MembreUpdateView.as_view()), name='membre_update'),
    path('membres/<int:pk>/activer/emprunteur', bibliothecaire_required(views.MembreActivateEmprunteurView.as_view()), name='membre_activate_emprunteur'),
    path('membres/<int:pk>/supprimer/', bibliothecaire_required(views.MembreDeleteView.as_view()), name='membre_delete'),
    path("membres/<int:pk>/emprunter", bibliothecaire_required(EmpruntCreateFromMembreView.as_view()), name="membre_emprunter"),
    path("membres/<int:pk>/rendre/", bibliothecaire_required(EmpruntRendreFromMembreView.as_view()), name="membre_rendre"),

    # Fonctionnalités souhaitables (optionnelles)
#    path('medias/<int:pk>/supprimer/', bibliothecaire_required(views.MediaDeleteView.as_view()), name='media_delete'),
#    path('membres/<int:pk>/historique/', bibliothecaire_required(views.MembreHistoriqueView.as_view()), name='membre_historique'),
    path('jeux/', bibliothecaire_required(views.JeuListView.as_view()), name='jeu_list'),
    path('jeux/ajouter/', bibliothecaire_required(views.JeuCreateView.as_view()), name='jeu_create'),
    path('jeux/<int:pk>/', bibliothecaire_required(views.JeuDetailView.as_view()), name='jeu_detail'),
    path('jeux/<int:pk>/modifier/', bibliothecaire_required(views.JeuUpdateView.as_view()), name='jeu_update'),

    # Fonctionnalités de DEBUG pour rejeu UX
    path("rejeu-ux/retard/reset-session/", bibliothecaire_required(ResetRetardSessionView.as_view()), name="rejeu_reset_retard_session"),
]
