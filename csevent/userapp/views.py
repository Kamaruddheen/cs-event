from django.shortcuts import render, redirect
from verify_email.email_handler import send_verification_email

from .models import *
from .forms import *


def signup(request):
    form = UserForm(request.POST or None)
    form1 = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid() and form1.is_valid():
        form_obj = send_verification_email(request, form)
        print(form_obj)
        """form_obj = form.save(commit=False)
        form_obj.user_type = 3
        form_obj.save()"""
        # Student Form
        from1_obj = form1.save(commit=False)
        from1_obj.user = User.objects.get(id=form_obj.id)
        from1_obj.save()

        return redirect('homepage')

    content = {
        'form': form, 'form1': form1
    }

    return render(request, 'userapp/registration.html', context=content)


def myaccount(request):
    pass

# Registration Page


def event_register(request):
    return render(request, "userapp/event_register.html")


def demo_link(request):
    return render(request, "userapp/event_test.html")


def register_codetreasure(request):
    # stu_obj = StudentModel.objects.update(
    #     user=request.user, is_codetreasure=True)
    return render(request, "userapp/event_register.html")


def register_impreza(request):
    stu_obj = StudentModel.objects.update(
        user=request.user, is_impreza=True)
    return render(request, "userapp/event_register.html")


def register_webdodger(request):
    stu_obj = StudentModel.objects.update(
        user=request.user, is_webdodger=True)
    return render(request, "userapp/event_register.html")


def register_ransack(request):
    event = "ransack"
    stu_obj = StudentModel.objects.update(
        user=request.user, is_ransack=True)

    # Prelims_Test() Model
    # crate(user, event_choice, tst_status=notstart, attend [default=false])
    #

    return render(request, "userapp/event_register.html")


def register_geekspeak(request):
    stu_obj = StudentModel.objects.update(
        user=request.user, is_geekspeak=True)
    return render(request, "userapp/event_register.html")
