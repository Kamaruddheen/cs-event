from django.contrib import messages
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from userapp.models import *


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
        question_set = question_model.objects.all().order_by('id')
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
    question_set = final_code_shuffle_relation.objects.all().order_by('id')
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
    question_set = final_code_binary_question.objects.all().order_by('id')
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
    question_set = final_code_spot_error_question.objects.all().order_by('id')
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
    #  prelims test (end,test_status)

    return HttpResponse('Successful test completion')


# Cheated Finals
def finals_exit_test(request):
    messages.warning(request, "Tab Switch Deteched")
    status = True

    if request.method == "POST":
        final_test.objects.filter(
            student=request.user, event="codetreasure").update(test_status="cheated")

    data = {
        'is_taken': status
    }
    return JsonResponse(data)


# Cheated Prelims
def prelims_exit_test(request):
    messages.warning(request, "Tab Switch Deteched")
    status = True

    if request.method == "POST":
        prelim_test.objects.filter(
            Student=request.user, event="codetreasure").update(test_status="cheated")

    data = {
        'is_taken': status
    }
    return JsonResponse(data)


# Finals Score Entry
def finals_score(request):
    code_score = final_answer_relation.objects.all()

    if request.method == "POST":
        email = request.POST.get('email')
        email_id = request.POST.get('email_id')
        answer = request.POST.get('answer')
        if email:
            id = get_object_or_404(User, email=email)
            code_score = final_answer_relation.objects.filter(
                student=id).order_by('when')
        elif email_id:
            id = get_object_or_404(User, email=email_id)
            Score_codetreasureModel.objects.create(
                student=id, roundtype="final", score=answer)

    context = {
        'code_score': code_score
    }

    return render(request, "codetreasure/final_score.html", context=context)


# Prelims Score Entry
def prelims_score(request):
    code_score = None
    # Colleting the Email id for Prelims Result
    query = Stud_Res_CodeTreasure_Prelm.objects.values('student').distinct()

    for a in query:
        for k, id in a.items():
            user_obj = get_object_or_404(User, id=id)
            # Counting the Score for each user
            score = Stud_Res_CodeTreasure_Prelm.objects.filter(
                student=id, status=True).count()
            if not Score_codetreasureModel.objects.filter(student=user_obj, roundtype="prelims").exists():
                Score_codetreasureModel.objects.create(
                    student=user_obj, roundtype="prelims", score=score)

    code_score = Score_codetreasureModel.objects.filter(
        roundtype="prelims").order_by('-score')

    content = {
        'code_score': code_score
    }

    return render(request, "codetreasure/prelims_score.html", context=content)
