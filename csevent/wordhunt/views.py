from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .forms import *
from .models import *
from userapp.models import *


# Wordhunt Prelims Section A
def question_prelims_sectionA(request):#If condition for time checking adn update as started
    answer_form = Student_Answer(request.POST or None)

    section = True

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(
        roundtype="prelims", section="A").order_by('id')
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


# Wordhunt Prelims Section A
def question_prelims_sectionB(request):
    # wordhunt_B = Wordhunt.objects.filter(roundtype="prelims", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = True

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(
        roundtype="prelims", section="B").order_by('id')
    pages = Paginator(question_set, 1)

    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'answer_form': answer_form, 'section': section, 'page': page, 'pages': pages
    }

    return render(request, 'wordhunt/questionB.html', context=context)


# Wordhunt Prelims Section A
def question_finals_sectionA(request):
    # wordhunt_A = Wordhunt.objects.filter(roundtype="final", section="A")
    answer_form = Student_Answer(request.POST or None)

    section = False

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(
        roundtype="final", section="A").order_by('id')
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


# Wordhunt Prelims Section A
def question_finals_sectionB(request):
    # wordhunt_B = Wordhunt.objects.filter(roundtype="final", section="B")
    answer_form = Student_Answer(request.POST or None)

    section = False

    page_no = request.GET.get('page', 1)
    question_set = Wordhunt.objects.filter(
        roundtype="final", section="B").order_by('id')
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


# All Prelims & Finals Answer will come here
def answer_submit(request):
    attended = False
    status = False
    student = request.user
    question_id = request.POST.get('question_id', None)
    question_obj = get_object_or_404(Wordhunt, id=question_id)
    actual_answer = (request.POST.get('answer', None)).lower()
    value = ((request.POST.get('answer', None)).lower()).replace(" ", "")

    if question_obj.correct_answer.lower() == value:
        #print(value, question_id, question_obj.correct_answer)
        status = True

    if Stud_Res_WordHunt.objects.filter(student=student, question=question_obj).exists():
        attended = True
        messages.info(request, "You have already attended this question")
    else:#answer entry
        student_final_answer = Stud_Res_WordHunt.objects.create(
            student=student, question=question_obj, user_answer=actual_answer, status=status)

    data = {
        'is_taken': attended}
    return JsonResponse(data)


# Cheated Prelims & Finals
def exit_test(request):
    messages.warning(request, "Tab Switch Deteched")
    status = True

    if request.method == "POST":
        round = request.POST.get('round')
        if round == "prelims":
            prelim_test.objects.filter(
                Student=request.user, event="wordhunt").update(test_status="cheated")
        elif round == "finals":
            final_test.objects.filter(
                student=request.user, event="wordhunt").update(test_status="cheated")

    data = {
        'is_taken': status
    }
    return JsonResponse(data)


def finished_test(request):#status need to be changed for time
    return HttpResponse("Test completed successfully.")


# Student Result
def export_prelims(request):
    pass
