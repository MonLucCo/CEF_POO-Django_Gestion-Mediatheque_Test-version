from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

from bibliothecaire.models import Bibliothecaire
from mediatheque.common.logging import get_request_logger

logger = get_request_logger(__name__)


def bibliothecaire_required(view_func):
    """
    Décorateur pour restreindre l'accès aux vues de l'app 'bibliothecaire'
    sans distinction de rôle.
    - Vérifie que l'utilisateur est connecté.
    - Vérifie qu'il est lié à un objet Bibliothecaire (ADMIN ou GESTION).
    - Ajoute les logs INFO et WARNING standardisés pour refus/acceptation.
    - Redirige vers une page 302 d'information en cas de refus.
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect(reverse("accounts:403"))
            logger.warning("[ACCESS_DENIED] utilisateur=anonyme",
                           request=request, status_code=response.status_code,
                           content_length=len(response.content))
            return response

        try:
            request.user.bibliothecaire
        except Bibliothecaire.DoesNotExist:
            response = redirect(reverse("accounts:403"))
            logger.warning(f"[ACCESS_DENIED] utilisateur={request.user} (non bibliothécaire)",
                           request=request, status_code=response.status_code,
                           content_length=len(response.content))
            return response

        response = view_func(request, *args, **kwargs)
        length = response.get('Content-Length', 0)
        logger.info(f"[ACCESS_GRANTED] utilisateur={request.user.username}",
                    request=request, status_code=response.status_code,
                    content_length=length)
        return response

    return _wrapped_view
