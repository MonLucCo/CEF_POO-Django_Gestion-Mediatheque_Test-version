# bibliothecaire/mixins.py

from django.views.generic import ListView

class OrigineSessionMixin:
    origine_key = None

    def get(self, request, *args, **kwargs):
        if self.origine_key is None:
            raise ValueError("OrigineSessionMixin nécessite de définir 'origine_key' pour être utilisé.")
        request.session["liste_origine"] = self.origine_key
        return super().get(self, request, *args, **kwargs)
