from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from .image import meta_data


# Poster Prelims
def poster_prelims(request):
    form = PosterForm()
    if request.method == 'POST':
        if Poster.objects.filter(student=request.user, roundtype="prelims").exists():
            messages.info(
                request, "You have already uploaded your Documnet")
            return redirect('imageupload:poster_prelims')
        else:
            form = PosterForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.student = request.user
                obj.status = False
                obj.roundtype = "prelims"
                obj.save()
                return redirect('imageupload:success')
    return render(request, 'imageupload/poster.html', {'form': form})


# Poster Finals
def poster_finals(request):
    form = PosterForm()
    if request.method == 'POST':
        if Poster.objects.filter(student=request.user, roundtype="final").exists():
            messages.info(
                request, "You have already uploaded your Documnet")
            return redirect('imageupload:poster_finals')
        else:
            form = PosterForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.student = request.user
                obj.status = False
                obj.roundtype = "final"
                obj.save()
                return redirect('imageupload:success')
    return render(request, 'imageupload/poster.html', {'form': form})


# Logo Prelims
def logo_prelims(request):
    form = LogoForm()
    if request.method == 'POST':
        if Logo.objects.filter(student=request.user, roundtype="prelims").exists():
            messages.info(
                request, "You have already uploaded your Documnet")
            return redirect('imageupload:logo_prelims')
        else:
            form = LogoForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.student = request.user
                obj.status = False
                obj.roundtype = "prelims"
                # meta_data()
                obj.save()
                return redirect('imageupload:success')
    return render(request, 'imageupload/logo.html', {'form': form})


# Logo Finals
def logo_finals(request):
    form = LogoFinalForm()
    if request.method == 'POST':
        if Logo.objects.filter(student=request.user, roundtype="final").exists():
            messages.info(
                request, "You have already uploaded your Documnet")
            return redirect('imageupload:logo_finals')
        else:
            form = LogoFinalForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.student = request.user
                obj.status = False
                obj.roundtype = "final"
                # meta_data()
                obj.save()
                return redirect('imageupload:success')
    return render(request, 'imageupload/logo.html', {'form': form})


#  Status
def success(request):
    return HttpResponse('successfully uploaded')


def verify_meta_img(request):
    Result = Poster.objects.all()

    print()

    context = {'form': True}

    return render(request, 'imageupload/logo.html', context)


# def display_logo(request):

#     if request.method == 'GET':

#         # getting all the objects of hotel.
#         Hotels = Hotel.objects.all()
#         return render((request, 'display_hotel_images.html',
#                        {'hotel_images': Hotels}))


# def display_poster(request):

#     if request.method == 'GET':

#         # getting all the objects of hotel.
#         Hotels = Hotel.objects.all()
#         return render((request, 'display_hotel_images.html',
#                        {'hotel_images': Hotels}))
