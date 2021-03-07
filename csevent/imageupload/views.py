from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from .image import meta_data


# Poster Prelims
def poster_prelims(request):
    form = PosterForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = PosterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.student = request.user
            obj.status = False
            obj.roundtype = "prelims"
            # meta_data()
            obj.save()
            # call the meta_data() function here with the image location and store it in the status field.
            return redirect('imageupload:success')
    return render(request, 'imageupload/poster.html', {'form': form})


# Poster Finals
def poster_finals(request):
    form = PosterForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = PosterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.student = request.user
            obj.status = False
            obj.roundtype = "final"
            # meta_data()
            obj.save()
            # call the meta_data() function here with the image location and store it in the status field.
            return redirect('imageupload:success')
    return render(request, 'imageupload/poster.html', {'form': form})


# Logo
def logo_prelims(request):
    form = LogoForm()
    if request.method == 'POST':
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


def logo_finals(request):
    form = LogoForm()
    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)

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
