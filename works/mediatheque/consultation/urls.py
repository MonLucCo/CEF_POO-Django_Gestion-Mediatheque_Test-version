from django.urls import path
from .views import AccueilConsultationView, SupportListView

urlpatterns = [
    path('', AccueilConsultationView.as_view(), name='accueil'),
    path('accueil/', AccueilConsultationView.as_view(), name='accueil'),
    path('supports/', SupportListView.as_view(), name='supports'),
    path('supports/medias/', SupportListView.as_view(), name='supports_medias'),
    path('supports/jeux/', SupportListView.as_view(), name='supports_jeux'),
    path('supports/medias/disponibles', SupportListView.as_view(), name='supports_medias_disponibles'),
    path('supports/vide', SupportListView.as_view(), name='supports_vide'),
]
