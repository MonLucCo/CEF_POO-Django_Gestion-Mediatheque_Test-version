from django.urls import path
from .views import accueil, CustomLoginView, CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('', accueil, name='accueil'),
    path('accueil/', accueil, name='accueil'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]