from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path('pre-registro/', views.pre_registro, name="pre_registro"),
    path('envio-email-pre-registro/', views.envio_email_pre_registro, name="envio_email_pre_registro"),
    path('confirmacao/', views.confirmar_cadastro, name="confirmar_cadastro"),
    path('cadastro-finalizado/', views.cadastro_finalizado, name="cadastro_finalizado"),
]
