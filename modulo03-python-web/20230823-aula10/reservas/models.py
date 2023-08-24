from django.db import models

from django.contrib.auth.models import User
from unidades.models import Unidade


class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    inicio_da_reserva = models.DateTimeField()
    final_da_reserva = models.DateTimeField()
    observacoes = models.TextField()

    class Meta:
        db_table = "tb_reservas"