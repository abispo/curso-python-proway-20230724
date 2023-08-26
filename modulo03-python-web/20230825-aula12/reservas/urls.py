
from django.urls import path

from . import views

app_name = "reservas"

urlpatterns = [
    path(
        'hospedes/<int:hospede_id>/',
        views.reservas_por_hospede,
        name="reservas_por_hospede"
    ),
]
