from django.contrib import messages
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


def register_codetreasure(request):
    # registering this event
    stu_obj = StudentModel.objects.update(
        user=request.user, is_codetreasure=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='codetreasure').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='codetreasure', test_status='not_started')
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/event_register.html")
    return render(request, "userapp/event_register.html")


def register_impreza(request):
    # registering this event
    stu_obj = StudentModel.objects.update(
        user=request.user, is_impreza=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='logo').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='logo', test_status='not_started')
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/event_register.html")
    return render(request, "userapp/event_register.html")


def register_webdodger(request):
    # registering this event
    StudentModel.objects.update(user=request.user, is_webdodger=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='poster').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='poster', test_status='not_started')
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/event_register.html")
    return render(request, "userapp/event_register.html")


def register_ransack(request):
    # registering this event
    StudentModel.objects.update(user=request.user, is_ransack=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='wordhunt').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='wordhunt', test_status='not_started')
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/event_register.html")

    return render(request, "userapp/event_register.html")


def register_geekspeak(request):
    # registering this event
    stu_obj = StudentModel.objects.update(
        user=request.user, is_geekspeak=True)
    # registering event for test
    if not prelim_test.objects.filter(Student=request.user, event='ppt').exists():
        prelim_test.objects.create(Student=request.user,
                                   event='ppt', test_status='not_started')
    else:
        messages.info(request, "You have already registered for this Event")
        return render(request, "userapp/event_register.html")
    return render(request, "userapp/event_register.html")
