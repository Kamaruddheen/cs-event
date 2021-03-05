from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def question_prelims_view(request):
    wordhunt = Wordhunt.objects.filter(roundtype="prelims")
    answer_form = Student_Answer(request.POST or None)

    if request.method == "POST":
        question_id = request.POST.get('data-id')
        print(question_id)

        if answer_form.is_valid():
            answer_form.save(commit=False)
            answer_form.student = User.objects.get(id=request.user.id or None)

    context = {'questions': wordhunt, 'answer_form': answer_form}

    return render(request, 'wordhunt/question.html', context)
