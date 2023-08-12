from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Question

def index(request):

    # session.query(Question).order_by("-pub_date")
    # SELECT * FROM polls_question ORDER BY pub_date DESC
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"Você está na página de resultados da pergunta de id {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Você está acessando a página de votação da pergunta de id {question_id}.")
