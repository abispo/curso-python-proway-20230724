# Decorator que é utilizado para restringir o acesso à qualquer view apenas
# para usuários que estiverem autenticados no sistema
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, "core/index.html")


@login_required
def perfil_hospede(request):
    return render(request, "core/perfil_hospede.html")