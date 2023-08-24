from django.db import models

class TipoUnidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        db_table = "tb_tipos_unidade"


class Unidade(models.Model):
    nome = models.CharField(max_length=200)
    tipo_unidade = models.ForeignKey(TipoUnidade, on_delete=models.CASCADE)
    disponivel = models.BooleanField()
    preco = models.FloatField()
    descricao = models.TextField()

    class Meta:
        db_table = "tb_unidades"