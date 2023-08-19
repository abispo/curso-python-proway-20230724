from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email


def pre_registro(request):

    if request.method == "GET":    
        form = PreRegistroForm()

        return render(request, "registro/pre_registro.html", {"form": form})

    elif request.method == "POST":
        form = PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")

            # Verifica se o e-mail já está cadastrado na tabela de usuários
            email_ja_cadastrado = User.objects.filter(email=email)

            # Verifica se o e-mail já não está no pré-registro
            email_no_pre_registro = PreRegistro.objects.filter(email=email, valido=True)

            if email_ja_cadastrado or email_no_pre_registro:
                form.errors.update({
                    "Erro no pré-registro": "O e-mail informado não é válido. Verifique se você já não possui cadastro ou ainda não confirmou o pré-registro."
                })

                return render(request, "registro/pre_registro.html", {"form": form})
            
            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            # Enviar e-mail com o link de confirmação
            enviar_email(pre_registro)

            return redirect("registro:envio_email_pre_registro")


def envio_email_pre_registro(request):
    return render(request, "registro/envio_email_pre_registro.html")


def confirmar_cadastro(request):
    try:
        pre_registro = PreRegistro.objects.get(uuid=request.GET.get("id"))

        return render(request, "registro/registro.html", {"pre_registro": pre_registro})

    except PreRegistro.DoesNotExist:
        return render(request, "registro/falha_confirmacao_cadastro.html", {"erro": "Token de confirmação inexistente"})