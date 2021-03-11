from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import datetime
from .forms import *
from .models import *
from userapp.models import *


# Wordhunt Prelims Section A
def question_prelims_sectionA(request):
    #Get the actual start and end date and time of the event
    date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="preliminary")
    start=date_obj.start
    end=date_obj.end
    print(end < datetime.datetime.now())
    #Get the current date and time
    current=datetime.datetime.now()
    
    #Compare current with actual start and end date and time
    if start>current:
        return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})
    elif start<=current and current<=end:
        current_user_obj=get_object_or_404(prelim_test,Student=request.user,event='wordhunt')
        if current_user_obj.test_status=="not_started":
            prelim_test.objects.filter(Student=request.user,event='wordhunt').update(start=datetime.datetime.now(),test_status='started',attended=True)
        elif current_user_obj.test_status=='cheated':
            return render(request,'show_test.html',{'status':'cheated'})

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

    elif end<current:
        #test = after indicates test has completed already
        return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
    
    else:
        return HttpResponse("something wrong sorry for the inconvenience")


# Wordhunt Prelims Section A
def question_prelims_sectionB(request):
    #Get the actual start and end date and time of the event
    date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="preliminary")
    start=date_obj.start
    end=date_obj.end

    #Get the current datetime
    current=datetime.datetime.now()

    #Compare current with actual start and end date and time
    if start>current:
        return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})

    elif start<=current and current<=end:
        #Get the current user object
        current_user_obj=get_object_or_404(prelim_test,Student=request.user,event='wordhunt')
        if current_user_obj.test_status=='not_started':
            prelim_test.objects.filter(Student=request.user,event='wordhunt').update(start=datetime.datetime.now(),test_status='started',attended=True)
        elif current_user_obj.test_status=='cheated':
            return render(request,'show_test.html',{'status':'cheated'})
        
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
        
    elif end<current:
        #test = after indicates test has completed already
        return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
    
    else:
        return HttpResponse("something wrong sorry for the inconvenience")

# Wordhunt Prelims Section A
def question_finals_sectionA(request):
    #Get the actual start and end date and time of the event
    date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="final")
    start=date_obj.start
    end=date_obj.end
    
    #Get the current date and time
    current=datetime.datetime.now()

    #Compare current with actual start and end date and time
    if start>current:
        return render(request,'show_test.html',{'start':start,'end':end,'status':'before'})

    elif start<=current and current<=end:
        #Some other filtering
        current_user_obj=get_object_or_404(final_test,Student=request.user,event='wordhunt')
        if current_user_obj.test_status=="not_started":
            prelim_test.objects.filter(Student=request.user,event='wordhunt').update(start=datetime.datetime.now(),test_status='started',attended=True)
        elif current_user_obj.test_status=="cheated":
            return render(request,'show_test.html',{'status':'cheated'})    
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
    
    elif end<current:
        #test = after indicates test has completed already
        return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
    
    else:
        return HttpResponse("something wrong sorry for the inconvenience")

# Wordhunt Prelims Section A
def question_finals_sectionB(request):
    #Get the actual start and end date and time of the event
    date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="final")
    start=date_obj.start
    end=date_obj.end

    #Get the current date and time
    current=datetime.datetime.now()

    #Compare current with actual start and end date and time
    if start>current:
        return render(request,'show_test.html',{'start':start,'end':end,'status':'before'}) 
    
    elif start<=current and current<=end:
        #Some other filtering
        current_user_obj=get_object_or_404(final_test,Student=request.user,event='wordhunt')
        if current_user_obj.test_status=="not_started":
            prelim_test.objects.filter(Student=request.user,event='wordhunt').update(start=datetime.datetime.now(),test_status='started',attended=True)
        elif current_user_obj.test_status=="cheated":
            return render(request,'show_test.html',{'status':'cheated'})   
        
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
    elif end<current:
        #test = after indicates test has completed already
        return render(request,'show_test.html',{'start':start,'end':end,'status':'after'})
    else:
        return HttpResponse("something wrong sorry for the inconvenience")

# All Prelims & Finals Answer will come here
def answer_submit(request):
    #Get the round of the test :
    round=request.POST.get('round','something wrong')
    if round=='prelims':
        date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="preliminary")
        current_user_obj=get_object_or_404(prelim_test,Student=request.user,event='wordhunt')
    elif round=='finals':
        date_obj=get_object_or_404(test_timings,event="wordhunt",round_type="final")
        current_user_obj=get_object_or_404(final_test,Student=request.user,event='wordhunt')
        
    #Get the actual start and end date and time of the event
    start=date_obj.start
    end=date_obj.end
    
    attended = False
    status = False
    failure=True #indicates data is saved within the time or not
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
    else:
        #Answer entry is here
        current_time_during_submit=datetime.datetime.now()
        if start<=current_time_during_submit and current_time_during_submit<=end:
            #Checking for cheated
            if current_user_obj.test_status=='cheated':
                return JsonResponse({'status':'cheated'})
            else:    
                student_final_answer = Stud_Res_WordHunt.objects.create(
                    student=student, question=question_obj, user_answer=actual_answer, status=status)
                failure=False#indicates data is saved within the time

    data = {
        'is_taken': attended,
        'failure':failure}
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
