from django.urls import path
from . import views

app_name = 'bibliothecaire'

urlpatterns = [
    # Accueil
    path('', views.AccueilBibliothecaireView.as_view(), name='accueil'),
    path('accueil/', views.AccueilBibliothecaireView.as_view(), name='accueil'),

    # Media (Livre, Dvd, Cd)
    path('media/', views.MediaListView.as_view(), name='media_list'),
    path('media/<int:pk>/', views.MediaDetailView.as_view(), name='media_detail'),
#    path('media/ajouter/', views.MediaCreateView.as_view(), name='media_create'),
#    path('media/<int:pk>/modifier/', views.MediaUpdateView.as_view(), name='media_update'),
#    path('media/<int:pk>/supprimer/', views.MediaDeleteView.as_view(), name='media_delete'),

    # Emprunts
 #   path('emprunts/', views.EmpruntListView.as_view(), name='emprunt_list'),
 #   path('emprunts/ajouter/', views.EmpruntCreateView.as_view(), name='emprunt_create'),
 #   path('emprunts/<int:pk>/retour/', views.RetourUpdateView.as_view(), name='emprunt_retour'),

    # Membres
 #    path('membres/', views.MembreListView.as_view(), name='membre_list'),
 #   path('membres/ajouter/', views.MembreCreateView.as_view(), name='membre_create'),
 #   path('membres/<int:pk>/', views.MembreDetailView.as_view(), name='membre_detail'),
 #   path('membres/<int:pk>/modifier/', views.MembreUpdateView.as_view(), name='membre_update'),
 #   path('membres/<int:pk>/supprimer/', views.MembreDeleteView.as_view(), name='membre_delete'),

    # Fonctionnalités souhaitables (optionnelles)
 #   path('media/type/<str:type>/', views.MediaFilteredListView.as_view(), name='media_filtered'),
 #   path('emprunts/statut/<int:statut>/', views.EmpruntFilteredListView.as_view(), name='emprunt_filtered'),
 #   path('membres/<int:pk>/historique/', views.MembreHistoriqueView.as_view(), name='membre_historique'),
 #    path('jeux/', views.JeuListView.as_view(), name='jeu_list'),
 #   path('jeux/ajouter/', views.JeuCreateView.as_view(), name='jeu_create'),
 #   path('jeux/<int:pk>/', views.JeuDetailView.as_view(), name='jeu_detail'),
 #   path('jeux/<int:pk>/modifier/', views.JeuUpdateView.as_view(), name='jeu_update'),
]
