from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def prelm_question(request):

    if request.method == "POST":
        student = request.user
        q_id = request.POST.get('q_id', 'something wrong')
        question = get_object_or_404(question_model, id=q_id)
        if Stud_Res_CodeTreasure_Prelm.objects.filter(student=student, question=question).exists():
            return JsonResponse({'save': "something wrong"})
        else:
            user_answer = request.POST.get("answer", "No value")
            if user_answer == question.correct_option:
                status = True
            else:
                status = False
            obj = Stud_Res_CodeTreasure_Prelm.objects.create(
                student=student, question=question, user_answer=user_answer, status=status)
            return JsonResponse({'save': "completed"})
    else:
        page_no = request.GET.get('page', 1)
        question_set = question_model.objects.all()
        pages = Paginator(question_set, 1)

        try:
            page = pages.page(page_no)
        except EmptyPage:
            page = pages.page(pages.num_pages)
        except PageNotAnInteger:
            page = pages.page(1)

        context = {
            'page': page, 'pages': pages
        }
        # questions_list = question_model.objects.all().order_by('?')
        return render(request, 'codetreasure/prelm_question.html', context=context)


def final_code_shuffle_function(request):
    if request.method == "POST":
        student = request.user
        question = get_object_or_404(
            final_code_shuffle_relation, id=request.POST.get('q_id', 'something wrong'))
        if final_answer_relation.objects.filter(student=student, final_code_shuffle_question=question).exists():
            return JsonResponse({'result': "already entered"})
        else:
            user_answer = request.POST.get('answer', 'Something wrong')
            final_answer_relation.objects.create(
                student=student, final_code_shuffle_question=question, user_answer=user_answer)
            return JsonResponse({'result': 'success'})

    page_no = request.GET.get('page', 1)
    question_set = final_code_shuffle_relation.objects.all()
    pages = Paginator(question_set, 1)

    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'page': page, 'pages': pages
    }

    return render(request, 'codetreasure/final_code_shuffle.html', context=context)


def final_binary_function(request):
    if request.method == "POST":
        student = request.user
        question = get_object_or_404(
            final_code_binary_question, id=request.POST.get('q_id', 'something wrong'))
        if final_answer_relation.objects.filter(student=student, final_code_binary_question=question).exists():
            return JsonResponse({'result': 'already entered'})
        else:
            user_answer = request.POST.get('answer', 'something wrong')
            final_answer_relation.objects.create(
                student=student, final_code_binary_question=question, user_answer=user_answer)
            return JsonResponse({'result': 'success'})

    page_no = request.GET.get('page', 1)
    question_set = final_code_binary_question.objects.all()
    pages = Paginator(question_set, 1)

    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    return render(request, 'codetreasure/final_binary.html', {'page': page, 'pages': pages})


def final_spot_error_function(request):
    if request.method == 'POST':
        student = request.user
        question = get_object_or_404(final_code_spot_error_question, id=request.POST.get(
            'q_id', 'something went wrong'))
        if final_answer_relation.objects.filter(student=student, final_code_spot_error_question=question).exists():
            return JsonResponse({'result': 'already entered'})
        else:
            user_answer = request.POST.get('answer', 'something went wrong')
            final_answer_relation.objects.create(
                student=student, final_code_spot_error_question=question, user_answer=user_answer)
            return JsonResponse({'result': 'success'})

    page_no = request.GET.get('page', 1)
    question_set = final_code_spot_error_question.objects.all()
    pages = Paginator(question_set, 1)

    try:
        page = pages.page(page_no)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    except PageNotAnInteger:
        page = pages.page(1)

    context = {
        'page': page, 'pages': pages
    }
    return render(request, 'codetreasure/final_spot_error.html', context=context)


def last_binary_question(request):
    return HttpResponse('Successful test completion')


def prelm_status(request):
    return HttpResponse('Successful test completion')
