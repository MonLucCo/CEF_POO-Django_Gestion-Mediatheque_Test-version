from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse

from bibliothecaire.models import Bibliothecaire


def bibliothecaire_required(view_func):
    """
    Décorateur pour restreindre l'accès aux vues de l'app 'bibliothecaire'
    sans distinction de rôle.
    - Vérifie que l'utilisateur est connecté.
    - Vérifie qu'il est lié à un objet Bibliothecaire (ADMIN ou GESTION).
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        try:
            request.user.bibliothecaire
        except Bibliothecaire.DoesNotExist:
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    # return login_required(_wrapped_view)
    return _wrapped_view
