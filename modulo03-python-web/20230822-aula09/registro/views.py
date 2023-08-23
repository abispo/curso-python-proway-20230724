from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils import timezone

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email
from registro.validators import dados_preenchidos, username_ou_email_ja_existem, senhas_conferem


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

        if request.method == "GET":

            # Pegando os dados via query string
            # SELECT * FROM tb_pre_registro WHERE uuid = ?
            pre_registro = PreRegistro.objects.get(uuid=request.GET.get("id"))

            error = None

            if not pre_registro.valido:
                error = "O token de confirmação já foi utilizado."

            if (timezone.now() - pre_registro.data_hora).total_seconds() > settings.PRE_REGISTRO_TIME_LIMIT:
                error = "O token expirou. Refaça o pré-registro"
                pre_registro.valido = False
                pre_registro.save()

            if error:
                return render(
                    request,
                    "registro/falha_confirmacao_cadastro.html",
                    {"error": error}
                )

            return render(request, "registro/registro.html", {"pre_registro": pre_registro})
        
        elif request.method == "POST":

            username = request.POST["username"]
            email = request.POST["user_email"]
            primeiro_nome = request.POST["first_name"]
            senha = request.POST["password1"]
            confirmacao_senha = request.POST["password2"]
            pre_registro_uuid = request.POST["pre_registro_uuid"]

            pre_registro = PreRegistro.objects.get(uuid=pre_registro_uuid)

            error = None

            if not dados_preenchidos(username, primeiro_nome, senha, confirmacao_senha, pre_registro_uuid):
                error = "Você deve preencher todos os campos do formulário"

            if username_ou_email_ja_existem(username, email):
                error = "Existe algum problema com o seu cadastro. Verifique se o email ou o username já não existem."

            if not senhas_conferem(senha, confirmacao_senha):
                error = "A senha é diferente da confirmação de senha"

            if error:
                return render(
                    request,
                    "registro/registro.html",
                    {
                        "error": error,
                        "pre_registro": pre_registro
                    }
                )
            
            User.objects.create_user(
                username=username,
                email=email,
                password=senha,
                first_name=primeiro_nome
            )

            pre_registro.valido = False
            pre_registro.save()

            return redirect("registro:cadastro_finalizado")

    except (PreRegistro.DoesNotExist, ValidationError):
        return render(request, "registro/falha_confirmacao_cadastro.html", {"error": "Token de confirmação inexistente"})


def cadastro_finalizado(request):
    return render(request, "registro/cadastro_finalizado.html")
