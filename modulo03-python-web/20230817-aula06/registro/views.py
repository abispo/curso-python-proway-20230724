from django.shortcuts import render

from registro.forms import PreRegistroForm


def pre_registro(request):
    
    form = PreRegistroForm()

    return render(request, "registro/pre_registro.html", {"form": form})
