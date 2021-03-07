from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.
def prelm_question(request):
    
    if request.method=="POST":
        student=request.user
        q_id=request.POST.get('q_id','something wrong')
        question=get_object_or_404(question_model,id=q_id)
        if Stud_Res_CodeTreasure_Prelm.objects.filter(student=student,question=question).exists():
            return JsonResponse({'save':"something wrong"})
        else:
            user_answer=request.POST.get("answer","No value")
            if user_answer==question.correct_option:
                status=True
            else:
                status=False
            obj=Stud_Res_CodeTreasure_Prelm.objects.create(student=student,question=question,user_answer=user_answer,status=status)
            return JsonResponse({'save':"completed"})
    else:
        questions_list=question_model.objects.all().order_by('?')
        return render(request,'question/prelm_question.html',{'question':questions_list})

def final_code_shuffle_function(request):
    if request.method=="POST":
        student=request.user
        question=get_object_or_404(final_code_shuffle_relation,id=request.POST.get('q_id','something wrong'))
        if final_answer_relation.objects.filter(student=student,final_code_shuffle_question=question).exists():
            return JsonResponse({'result':"already entered"})
        else:
            user_answer=request.POST.get('answer','Something wrong')
            final_answer_relation.objects.create(student=student,final_code_shuffle_question=question,user_answer=user_answer)
            return JsonResponse({'result':'success'})
    queryset=final_code_shuffle_relation.objects.all().order_by('?')
    return render(request,'question/final_code_shuffle.html',{'queryset':queryset})

def final_binary_function(request):
    if request.method=="POST":
        student=request.user
        question=get_object_or_404(final_code_binary_question,id=request.POST.get('q_id','something wrong'))
        if final_answer_relation.objects.filter(student=student,final_code_binary_question=question).exists():
            return JsonResponse({'result':'already entered'})
        else:
            user_answer=request.POST.get('answer','something wrong')
            final_answer_relation.objects.create(student=student,final_code_binary_question=question,user_answer=user_answer)
            return JsonResponse({'result':'success'})
    question_set=final_code_binary_question.objects.all().order_by('?')
    return render(request,'question/final_binary.html',{'question_set':question_set})

def final_spot_error_function(request):
    if request.method=='POST':
        student=request.user
        question=get_object_or_404(final_code_spot_error_question,id=request.POST.get('q_id','something went wrong'))
        if final_answer_relation.objects.filter(student=student,final_code_spot_error_question=question).exists():
            return JsonResponse({'result':'already entered'})
        else:
            user_answer=request.POST.get('answer','something went wrong')
            final_answer_relation.objects.create(student=student,final_code_spot_error_question=question,user_answer=user_answer)
            return JsonResponse({'result':'success'})
    question_set=final_code_spot_error_question.objects.all().order_by('?')
    return render(request,'question/final_spot_error.html',{'question_set':question_set})
