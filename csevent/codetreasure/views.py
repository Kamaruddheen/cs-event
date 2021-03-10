from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from userapp.models import test_timings,prelim_test,final_test
import datetime

def prelm_question(request):
    #Event actual timings(date and time)
    date_obj=get_object_or_404(test_timings,event="codetreasure",round_type="preliminary")
    start=date_obj.start
    end=date_obj.end
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
            
            #Before sumitting the answer this if checks whether the time exceeds or not
            current_time_during_submit=datetime.datetime.now()
            if start<=current_time_during_submit and current_time_during_submit<=end:
                obj = Stud_Res_CodeTreasure_Prelm.objects.create(
                student=student, question=question, user_answer=user_answer, status=status)
                return JsonResponse({'save': "completed"})
            else: 
                return JsonResponse({'save':'after'})
    
    else:
        #Current date and time
        current=datetime.datetime.now()
        if start>current:
            return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})
            #status = True indicates test still exist
        elif start<=current and current<=end:
            current_user_obj=get_object_or_404(prelim_test,Student=request.user)
            #Update prelim_test model for the particular user
            if current_user_obj.test_status=="not_started":
                prelim_test.objects.filter(Student=request.user).update(start=datetime.datetime.now(),test_status='started',attended=True)
            elif current_user_obj.test_status=="cheated":
                return HttpResponse('cheated') 

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
        elif end<current:
            #test = False indicates test has completed already
            return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
        else:
            return HttpResponse("something wrong sorry for the inconvenience")

        


def final_code_shuffle_function(request):
    #Event actual timings(date and time)
    date_obj=get_object_or_404(test_timings,event="codetreasure",round_type="final")
    start=date_obj.start
    end=date_obj.end
    
    if request.method == "POST":
        student = request.user
        question = get_object_or_404(
            final_code_shuffle_relation, id=request.POST.get('q_id', 'something wrong'))
        
        #Checks whether this question is already entered by the user
        if final_answer_relation.objects.filter(student=student, final_code_shuffle_question=question).exists():
            return JsonResponse({'result': "already entered"})
        
        else:
            user_answer = request.POST.get('answer', 'Something wrong')
            
            #Checks whether the time is exhausted or not before submitting the answers
            current_time_during_submit=datetime.datetime.now()
            if start<=current_time_during_submit and current_time_during_submit<=end:
                obj = final_answer_relation.objects.create(
                student=student, final_code_shuffle_question=question, user_answer=user_answer)
                return JsonResponse({'result': "completed"})
            else: 
                return JsonResponse({'result':'after'})

    else:
        #Current time the finalists clicked the event
        current=datetime.datetime.now()
        #Checking if they before start the test
        if start>current:
            return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})
        
        elif start<=current and current<=end:
            current_user_obj=get_object_or_404(final_test,student=request.user)
            #Update final_test model for the particular user
            if current_user_obj.test_status=="not_started":
                final_test.objects.filter(student=request.user).update(start=datetime.datetime.now(),test_status='started',attended=True)
            elif current_user_obj.test_status=="cheated":
                return HttpResponse('cheated') 

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
        elif end<current:
            #test = False indicates test has completed already
            return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
        else:
            return HttpResponse("something wrong sorry for the inconvenience")


def final_binary_function(request):
    #Event actual timings(date and time)
    date_obj=get_object_or_404(test_timings,event="codetreasure",round_type="final")
    start=date_obj.start
    end=date_obj.end

    if request.method == "POST":
        student = request.user
        question = get_object_or_404(
            final_code_binary_question, id=request.POST.get('q_id', 'something wrong'))
        if final_answer_relation.objects.filter(student=student, final_code_binary_question=question).exists():
            return JsonResponse({'result': 'already entered'})
        else:
            user_answer = request.POST.get('answer', 'something wrong')
            current_time_during_submit=datetime.datetime.now()
            if start<=current_time_during_submit and current_time_during_submit<=end:
                final_answer_relation.objects.create(
                    student=student, final_code_binary_question=question, user_answer=user_answer)
                return JsonResponse({'result': 'completed'})
            else:
                return JsonResponse({'result':'after'})
            
    else:
        #Current time the finalists clicked the event
        current=datetime.datetime.now()
        #Checking if they before start the test
        if start>current:
            return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})
        elif start<=current and current<=end:
            current_user_obj=get_object_or_404(final_test,student=request.user)
            #Update final_test model for the particular user
            if current_user_obj.test_status=="not_started":
                final_test.objects.filter(student=request.user).update(start=datetime.datetime.now(),test_status='started',attended=True)
            elif current_user_obj.test_status=="cheated":
                return HttpResponse('cheated') 
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
        elif end<current:
            #test = False indicates test has completed already
            return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
        else:
            return HttpResponse("something wrong sorry for the inconvenience")


def final_spot_error_function(request):
    #Event actual timings(date and time)
    date_obj=get_object_or_404(test_timings,event="codetreasure",round_type="final")
    start=date_obj.start
    end=date_obj.end

    if request.method == 'POST':
        student = request.user
        question = get_object_or_404(final_code_spot_error_question, id=request.POST.get(
            'q_id', 'something went wrong'))
        if final_answer_relation.objects.filter(student=student, final_code_spot_error_question=question).exists():
            return JsonResponse({'result': 'already entered'})
        else:
            user_answer = request.POST.get('answer', 'something went wrong')
            current_time_during_submit=datetime.datetime.now()
            if start<=current_time_during_submit and current_time_during_submit<=end:
                final_answer_relation.objects.create(
                    student=student, final_code_spot_error_question=question, user_answer=user_answer)
                return JsonResponse({'result': 'completed'})
            else:
                return JsonResponse({'result':'after'})
    else:
        #Current date with time the finalists clicked the event
        current=datetime.datetime.now()
        #Checking if they before start the test
        if start>current:
            return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})
        elif start<=current and current<=end:
            current_user_obj=get_object_or_404(final_test,student=request.user)
             #Update final_test model for the particular user
            if current_user_obj.test_status=="not_started":
                final_test.objects.filter(student=request.user).update(start=datetime.datetime.now(),test_status='started',attended=True)
            elif current_user_obj.test_status=="cheated":
                return HttpResponse('cheated') 
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
        elif end<current:
            #test = False indicates test has completed already
            return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
        else:
            return HttpResponse("something wrong sorry for the inconvenience")

#Final question hendling view
def last_question(request):
    final_test.objects.filter(student=request.user).update(end=datetime.datetime.now(),test_status='finished')
    return HttpResponse('Successful test completion')


def exit_test(request):
    status = True
    data = {
        'is_taken': status
    }
    return JsonResponse(data)
