from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

def accueil(request):
    return render(request, 'accounts/accueil.html')


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True      # si déjà connecté, redirige vers accueil
    next_page = "accounts:accueil"          # redirection après login


class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = "accounts:accueil"          # redirection après logout
