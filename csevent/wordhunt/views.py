from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .forms import *
from .models import *


def question_prelims_view(request):
    wordhunt_A = Wordhunt.objects.filter(roundtype="prelims", section="A")
    wordhunt_B = Wordhunt.objects.filter(roundtype="prelims", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = True

    context = {'questionsA': wordhunt_A, 'questionsB': wordhunt_B,
               'answer_form': answer_form, 'section': section}

    return render(request, 'wordhunt/question.html', context)


def question_finals_view(request):
    wordhunt_A = Wordhunt.objects.filter(roundtype="final", section="A")
    wordhunt_B = Wordhunt.objects.filter(roundtype="final", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = False

    context = {'questionsA': wordhunt_A, 'questionsB': wordhunt_B,
               'answer_form': answer_form, 'section': section}

    return render(request, 'wordhunt/question.html', context)


def answer_submit(request):
    attended = False
    status = False
    student = request.user
    question_id = request.POST.get('question_id', None)
    question_obj = get_object_or_404(Wordhunt, id=question_id)
    actual_answer = (request.POST.get('answer', None)).lower()
    value = ((request.POST.get('answer', None)).lower()).replace(" ", "")

    if question_obj.correct_answer.lower() == value:
        print(value, question_id, question_obj.correct_answer)
        status = True

    if Stud_Res_WordHunt.objects.filter(student=student, question=question_obj).exists():
        attended = True
        messages.info(request, "You have already attended this question")
    else:
        student_final_answer = Stud_Res_WordHunt.objects.create(
            student=student, question=question_obj, user_answer=actual_answer, status=status)

    data = {
        'is_taken': attended}
    return JsonResponse(data)


def export_report(request):
    prelims_result = Stud_Res_WordHunt.objects.all()
