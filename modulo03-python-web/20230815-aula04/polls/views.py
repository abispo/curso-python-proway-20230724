from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Question, Choice

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

    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "Você deve escolher uma das opções"
        }
        return render(request, "polls/detail.html", context)
    
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    