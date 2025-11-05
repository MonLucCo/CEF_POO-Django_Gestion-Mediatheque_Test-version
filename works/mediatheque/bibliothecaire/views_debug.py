from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, timedelta

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

        return redirect("bibliothecaire:rejeu_reset_retard_session")
