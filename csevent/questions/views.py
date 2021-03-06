from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from random import shuffle
# Create your views here.
def prelm_question(request):
    questions_list=question.objects.all().order_by('?')
    if request.method=="POST":
        for q in questions_list:
            answer=request.POST.get(str(q.id),"No value")
            if answer==q.correct_option:
                status=True
            else:
                status=False
            obj=Stud_Res_CodeTreasure_Prelm.objects.create(student="harish",question=q,user_answer=answer,status=status)
        return HttpResponse("success")
    return render(request,'question/prelm_question.html',{'question':questions_list})