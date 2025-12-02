import logging

class RequestLoggerAdapter(logging.LoggerAdapter):
    """
    Adapter pour formater les logs applicatifs avec le contexte HTTP.
    Utilisation :
        adapter = RequestLoggerAdapter(logging.getLogger(__name__), {})
        adapter.info("[LOGIN] utilisateur=...", request=request, status_code=302)
    """
    def process(self, msg, kwargs):
        # Récupère 'request' si fourni, sinon None
        request = kwargs.pop("request", None)
        # Permet de passer explicitement le code (200, 302, etc.)
        status = kwargs.pop("status_code", "-")
        # Récupère la taille en octets de la réponse envoyée
        length = kwargs.pop("content_length", "-")

        if request is not None:
            method = getattr(request, "method", "-")
            path = getattr(request, "path", "-")
            # Construit un message homogène au style des logs de routage Django
            msg = f'"{method} {path} HTTP/1.1" {status} {length} : {msg}'
        else:
            # Fallback si pas de request fournie
            msg = f'"- -" {status} {msg}'

        return msg, kwargs

def get_request_logger(module_name: str) -> RequestLoggerAdapter:
    """
    Fournit un RequestLoggerAdapter pour le module donné.
    """
    base_logger = logging.getLogger(module_name)
    return RequestLoggerAdapter(base_logger, {})
