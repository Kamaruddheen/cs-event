from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .forms import *
from .models import *


def question_prelims_view(request):
    wordhunt = Wordhunt.objects.filter(roundtype="prelims")
    answer_form = Student_Answer(request.POST or None)

    context = {'questions': wordhunt, 'answer_form': answer_form}

    return render(request, 'wordhunt/question.html', context)


def question_finals_view(request):
    wordhunt = Wordhunt.objects.filter(roundtype="final")
    answer_form = Student_Answer(request.POST or None)

    context = {'questions': wordhunt, 'answer_form': answer_form}

    return render(request, 'wordhunt/question.html', context)


def answer_submit(request):
    attended = False
    status = False
    student = request.user
    question_id = request.POST.get('question_id', None)
    question_obj = get_object_or_404(Wordhunt, id=question_id)
    value = ((request.POST.get('answer', None)).lower()).replace(" ", "")

    if question_obj.correct_answer.lower() == value:
        print(value, question_id, question_obj.correct_answer)
        status = True

    if Stud_Res_WordHunt.objects.filter(student=student, question=question_obj).exists():
        attended = True
        messages.info(request, "You have already attended this question")
    else:
        student_final_answer = Stud_Res_WordHunt.objects.create(
            student=student, question=question_obj, user_answer=value, status=status)

    data = {
        'is_taken': attended}
    return JsonResponse(data)
