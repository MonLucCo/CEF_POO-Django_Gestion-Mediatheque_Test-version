from django.urls import path
from . import views
from .views import EmpruntCreateFromMembreView
from .views_debug import ResetRetardSessionView

app_name = 'bibliothecaire'

urlpatterns = [
    # Accueil
    path('', views.AccueilBibliothecaireView.as_view(), name='accueil'),
    path('accueil/', views.AccueilBibliothecaireView.as_view(), name='accueil'),

    # Media (Livre, Dvd, Cd)
    # Listes
    path('medias/', views.MediaListView.as_view(), name='media_list'),
    path('medias/consultables/', views.MediaListConsultableView.as_view(), name='media_list_consultables'),
    path('medias/disponibles/', views.MediaListDisponibleView.as_view(), name='media_list_disponibles'),
    path('medias/types/', views.MediaListByTypeView.as_view(), name='media_list_by_type'),
    path('medias/non-types/', views.MediaNonTypeListView.as_view(), name='media_list_non_types'),
    # Détails
    path('medias/<int:pk>/', views.MediaDetailView.as_view(), name='media_detail'),
    # Création
    path('medias/ajouter/', views.MediaCreateView.as_view(), name='media_create'),
    path('medias/ajouter/livre', views.MediaLivreCreateView.as_view(), name='media_create_livre'),
    path('medias/ajouter/dvd', views.MediaDvdCreateView.as_view(), name='media_create_dvd'),
    path('medias/ajouter/cd', views.MediaCdCreateView.as_view(), name='media_create_cd'),
    # Mise à jour
    path('medias/<int:pk>/modifier/', views.MediaUpdateView.as_view(), name='media_update'),
    path('medias/<int:pk>/modifier/livre/', views.MediaTypageLivreView.as_view(), name='media_typage_livre'),
    path('medias/<int:pk>/modifier/dvd/', views.MediaTypageDvdView.as_view(), name='media_typage_dvd'),
    path('medias/<int:pk>/modifier/cd/', views.MediaTypageCdView.as_view(), name='media_typage_cd'),

    path('medias/<int:pk>/livre/modifier/', views.LivreUpdateView.as_view(), name='media_update_livre'),
    path('medias/<int:pk>/dvd/modifier/', views.DvdUpdateView.as_view(), name='media_update_dvd'),
    path('medias/<int:pk>/cd/modifier/', views.CdUpdateView.as_view(), name='media_update_cd'),

    path('medias/<int:pk>/annuler_typage/', views.MediaCancelTypingView.as_view(), name='media_cancel_typing'),

    #    path('medias/<int:pk>/supprimer/', views.MediaDeleteView.as_view(), name='media_delete'),

    # Emprunts
     path('emprunts/', views.EmpruntListView.as_view(), name='emprunt_list'),
     path('emprunts/retards/', views.EmpruntRetardView.as_view(), name='emprunt_retard'),
     path('emprunts/ajouter/', views.EmpruntCreateView.as_view(), name='emprunt_create'),
 #   path('emprunts/<int:pk>/retour/', views.RetourUpdateView.as_view(), name='emprunt_retour'),

    # Membres
    path('membres/', views.MembreListView.as_view(), name='membre_list'),
    path('membres/liste', views.MembreEnGestionView.as_view(), name='membre_list_gestion'),
    path('membres/liste/emprunteurs', views.MembreEmprunteursView.as_view(), name='membre_list_emprunteurs'),
    path('membres/liste/supprimes', views.MembreArchivesView.as_view(), name='membre_list_archives'),
    path('membres/ajouter/', views.MembreCreateView.as_view(), name='membre_create'),
    path('membres/ajouter/emprunteur', views.MembreCreateEmprunteurView.as_view(), name='membre_create_emprunteur'),
    path('membres/<int:pk>/', views.MembreDetailView.as_view(), name='membre_detail'),
    path('membres/<int:pk>/modifier/', views.MembreUpdateView.as_view(), name='membre_update'),
    path('membres/<int:pk>/activer/emprunteur', views.MembreActivateEmprunteurView.as_view(), name='membre_activate_emprunteur'),
    path('membres/<int:pk>/supprimer/', views.MembreDeleteView.as_view(), name='membre_delete'),
    path("membres/<int:pk>/emprunter", EmpruntCreateFromMembreView.as_view(), name="membre_emprunter"),

    # Fonctionnalités souhaitables (optionnelles)
 #   path('medias/type/<str:type>/', views.MediaFilteredListView.as_view(), name='media_filtered'),
 #   path('emprunts/statut/<int:statut>/', views.EmpruntFilteredListView.as_view(), name='emprunt_filtered'),
 #   path('membres/<int:pk>/historique/', views.MembreHistoriqueView.as_view(), name='membre_historique'),
 #    path('jeux/', views.JeuListView.as_view(), name='jeu_list'),
 #   path('jeux/ajouter/', views.JeuCreateView.as_view(), name='jeu_create'),
 #   path('jeux/<int:pk>/', views.JeuDetailView.as_view(), name='jeu_detail'),
 #   path('jeux/<int:pk>/modifier/', views.JeuUpdateView.as_view(), name='jeu_update'),

    # Fonctionnalités de DEBUG pour rejeu UX
    path("rejeu-ux/retard/reset-session/", ResetRetardSessionView.as_view(), name="rejeu_reset_retard_session"),

]
