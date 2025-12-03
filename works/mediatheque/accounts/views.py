from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from mediatheque.common.logging import get_request_logger

logger = get_request_logger(__name__)

def accueil(request):
    return render(request, 'accounts/accueil.html')

def error_403_view(request):
    return render(request, "accounts/403.html") # code 302 car page d'information. Pas d'erreur HTTP

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True      # si déjà connecté, redirige vers accueil
    next_page = "accounts:accueil"          # redirection après login

    def form_valid(self, form):
        user = form.get_user()
        response = super().form_valid(form)
        length = response.get('Content-Length', 0)
        logger.info(f"[LOGIN] utilisateur={user.username}",
                    request=self.request, status_code=response.status_code,
                    content_length=length)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        length = response.get('Content-Length', 0)

        # ✅ Trace particulière (ligne 5 du tableau des logs)
        logger.warning("[LOGIN_INVALID] tentative de connexion",
                       request=self.request, status_code=response.status_code,
                       content_length=length)
        return response


class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = "accounts:accueil"          # redirection après logout

    def dispatch(self, request, *args, **kwargs):
        # Capture l'utilisateur avant que Django ne le déconnecte
        user = request.user if request.user.is_authenticated else None

        response = super().dispatch(request, *args, **kwargs)   # Déconnexion effective de l'utilisateur
        length = response.get('Content-Length', 0)

        # ✅ Trace particulière (ligne 6 du tableau des logs)
        if user:
            logger.info(f"[LOGOUT] utilisateur={user.username}",
                        request=request, status_code=response.status_code,
                        content_length=length)
        else:
            logger.warning("[LOGOUT_INVALID] utilisateur=anonyme",
                           request=request, status_code=response.status_code,
                           content_length=length)
        return response
