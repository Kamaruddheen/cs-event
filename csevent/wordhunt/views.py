from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .forms import *
from .models import *


def question_prelims_sectionA(request):
    # wordhunt_A = Wordhunt.objects.filter(roundtype="prelims", section="A")
    answer_form = Student_Answer(request.POST or None)

    section = True

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(roundtype="prelims", section="A")
    pages = Paginator(question_set, 1)
    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'answer_form': answer_form, 'section': section, 'page': page, 'pages': pages}

    return render(request, 'wordhunt/questionA.html', context=context)


def question_prelims_sectionB(request):
    # wordhunt_B = Wordhunt.objects.filter(roundtype="prelims", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = True

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(roundtype="prelims", section="B")
    pages = Paginator(question_set, 1)
    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'answer_form': answer_form, 'section': section, 'page': page, 'pages': pages}

    context = {
        'answer_form': answer_form, 'section': section}

    return render(request, 'wordhunt/questionB.html', context=context)


def question_finals_sectionA(request):
    # wordhunt_A = Wordhunt.objects.filter(roundtype="final", section="A")
    answer_form = Student_Answer(request.POST or None)

    section = False

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(roundtype="final", section="A")
    pages = Paginator(question_set, 1)
    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'answer_form': answer_form, 'section': section, 'page': page, 'pages': pages}

    return render(request, 'wordhunt/questionA.html', context=context)


def question_finals_sectionB(request):
    # wordhunt_B = Wordhunt.objects.filter(roundtype="final", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = False

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(roundtype="final", section="B")
    pages = Paginator(question_set, 1)
    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'answer_form': answer_form, 'section': section, 'page': page, 'pages': pages}

    return render(request, 'wordhunt/questionB.html', context=context)


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
