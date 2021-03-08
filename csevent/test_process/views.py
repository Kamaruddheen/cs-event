from django.shortcuts import render
from .models import prelim_test,final_test
# Create your views here.
def register_codetreasure_prelim_test(request):
    prelim_test.objects.create(student=request.user,event='code treasure',test_status='not started')
    