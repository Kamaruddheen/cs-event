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