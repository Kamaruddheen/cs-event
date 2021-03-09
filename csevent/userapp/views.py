from django.contrib import messages
from django.shortcuts import render, redirect
from verify_email.email_handler import send_verification_email

from .decorators import *
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
    form = User_Form(request.POST or None, instance=request.user)
    form1 = StudentForm(request.POST or None,
                        request.FILES or None, instance=request.user.student)

    if request.method == "POST":
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            messages.success(
                request, "Your Account details saved successfully")
            return redirect("myaccount", permanent=True)

    content = {
        'form': form, 'form1': form1
    }

    return render(request, 'userapp/myaccount.html', context=content)


# Registration Page
def event_register(request):
    return render(request, "userapp/event_register.html")

@is_student
def register_codetreasure(request):
    # registering this event
    StudentModel.objects.filter(user=request.user).update(is_codetreasure=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='codetreasure').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='codetreasure', test_status='not_started')
        messages.info(request, "Successfully registered for Code Treasure")
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/register_codetreasure.html")
    return render(request, "userapp/event_register.html")


def register_impreza(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # registering this event
        StudentModel.objects.filter(user=request.user).update(is_impreza=True)
        # registering event for test
        if not prelim_test.objects.filter(Student=request.user, event='logo').exists():
            prelim_test.objects.create(Student=request.user,
                                       event='logo', test_status='not_started')
            messages.info(request, "Successfully registered for Impreza")
        else:
            messages.info(request, "You have already registered for this Event")
            return render(request, "userapp/register_impreza.html")
    return render(request, "userapp/register_impreza.html")


def register_webdodger(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # registering this event
        StudentModel.objects.filter(user=request.user).update(is_webdodger=True)
        # registering event for test
        if not prelim_test.objects.filter(Student=request.user, event='poster').exists():
            prelim_test.objects.create(Student=request.user,
                                       event='poster', test_status='not_started')
            messages.info(request, "Successfully registered for Web Dodger")
        else:
            messages.info(request, "You have already registered for this Event")
            return render(request, "userapp/register_webdodger.html")
    return render(request, "userapp/register_webdodger.html")


def register_ransack(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # registering this event
        StudentModel.objects.filter(user=request.user).update(is_ransack=True)
        # registering event for test
        if not prelim_test.objects.filter(Student=request.user, event='wordhunt').exists():
            prelim_test.objects.create(Student=request.user,
                                       event='wordhunt', test_status='not_started')
            messages.info(request, "Successfully registered for Ransack")
        else:
            messages.info(request, "You have already registered for this Event")
            return render(request, "userapp/register_ransack.html")
    return render(request, "userapp/register_ransack.html")


def register_geekspeak(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # registering this event
        StudentModel.objects.filter(user=request.user).update(is_geekspeak=True)
        # registering event for test
        if not final_test.objects.filter(student=request.user, event='ppt').exists():
            final_test.objects.create(student=request.user,
                                      event='ppt', test_status='not_started', placed="notselected")
            messages.info(request, "Successfully registered for GeekSpeak")
        else:
            messages.info(request, "You have already registered for this Event")
            return render(request, "userapp/register_geekspeak.html")
    return render(request, "userapp/register_geekspeak.html")