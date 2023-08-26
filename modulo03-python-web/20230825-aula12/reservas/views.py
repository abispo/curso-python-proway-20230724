from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from reservas.models import Reserva


@login_required
def reservas_por_hospede(request, hospede_id):

    if request.user.id == hospede_id:
        reservas = Reserva.objects.filter(usuario__id=hospede_id)

        return render(
            request,
            "reservas/reservas_por_hospede.html",
            {"reservas": reservas}
        )

    else:
        return redirect("core:index")
