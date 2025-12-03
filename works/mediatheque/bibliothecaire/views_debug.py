from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, timedelta

from mediatheque.common.logging import get_request_logger

logger = get_request_logger(__name__)

class ResetRetardSessionView(View):
    template_name = "bibliothecaire/rejeu_ux/reset_retard_session.html"

    def get(self, request):
        current = request.session.get("retard_last_check_date")
        return render(request, self.template_name, {
            "current_date": current,
        })

    def post(self, request):
        try:
            nb_jours = int(request.POST.get("nb_jours", 1))
        except ValueError:
            nb_jours = 1

        current = request.session.get("retard_last_check_date")
        if current:
            new_date = date.fromisoformat(current) - timedelta(days=nb_jours)
        else:
            new_date = date.today() - timedelta(days=nb_jours)

        request.session["retard_last_check_date"] = str(new_date)
        messages.success(request, f"Date de marquage modifiée à {new_date.strftime('%d %B %Y')}.")

        response = redirect("bibliothecaire:rejeu_reset_retard_session")
        length = len(response.content) if hasattr(response, "content") else 0

        # ✅ Trace particulière (ligne 10 du tableau des logs)
        logger.info(
            f"[ResetRetardSession] utilisateur={request.user.username} "
            f"décalage={nb_jours} jour(s), nouvelle_date={new_date.isoformat()}",
            request=request,
            status_code=response.status_code,
            content_length=length,
        )

        return response