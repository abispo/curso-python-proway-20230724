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

        # Podemos criar permissões personalizadas dentro do Django.
        # Para isso, utilizamos a lista de tuplas permissions
        # Que deve ficar dentro do class Meta
        permissions = [
            # Cada tupla deve ter 2 valores: O primeiro é o nome da permissão, e o segundo
            # é a descrição
            # Temos que fazer o mesmo processo que fazemos quanto atualizamos uma model
            ("pode_reservar_pelo_site", "Permissão que autoriza o hospede a fazer a reserva pelo site.")
        ]

    def __str__(self):
        return f"{self.usuario.first_name} ({self.unidade.nome})"