from django.shortcuts import render

from polls.models import Choice, Question

def index(request):
    
    questions_count = Question.objects.count()
    choices_count = len(Choice.objects.all())

    context = {
        "questions_count": questions_count,
        "choices_count": choices_count
    }

    return render(request, "estatisticas/index.html", context)
