from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo ao site de enquetes. Essa é a página principal.")

def detail(request, question_id):
    return HttpResponse(f"Você está acessando a pergunta de id {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Você está na página de resultados da pergunta de id {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Você está acessando a página de votação da pergunta de id {question_id}.")
