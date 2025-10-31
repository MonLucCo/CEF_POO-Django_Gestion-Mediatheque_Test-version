# bibliothecaire/mixins.py

class OrigineSessionMixin:
    origine_key = None

    def get(self, request, *args, **kwargs):
        if self.origine_key is None:
            raise ValueError("OrigineSessionMixin nécessite de définir 'origine_key' pour être utilisé.")
        request.session["liste_origine"] = self.origine_key
        return super().get(self, request, *args, **kwargs)


class MembreSuppressionContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        membre = self.get_object()
        context["peut_etre_supprime"] = membre.peut_etre_supprime()
        return context
