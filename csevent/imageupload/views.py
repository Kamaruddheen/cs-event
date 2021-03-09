from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse

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

    context = {'form': True}

    return render(request, 'imageupload/logo.html', context)


# Cheated
def exit_test(request):
    messages.warning(request, "Tab Switch Deteched")

    status = True
    data = {
        'is_taken': status
    }
    return JsonResponse(data)


def display_logo_prelims(request):
    # getting all the objects of Logo .
    score = LogoScoreForm(request.POST or None)
    logo = Logo.objects.filter(roundtype="prelims").order_by('id')

    if request.method == "POST":
        question_id = get_object_or_404(Logo, id=request.POST.get('q_id'))
        Logo.objects.filter(id=question_id.id).update(
            score=request.POST.get('answer'))

        return JsonResponse({'result': 'Good'})

    context = {'logo': logo, 'score': score}

    return render(request, 'imageupload/display_logo.html', context=context)


def display_logo_finals(request):
    # getting all the objects of Logo .
    score = LogoScoreForm(request.POST or None)
    logo = Logo.objects.filter(roundtype="final").order_by('id')

    if request.method == "POST":
        question_id = get_object_or_404(Logo, id=request.POST.get('q_id'))
        Logo.objects.filter(id=question_id.id).update(
            score=request.POST.get('answer'))

        return JsonResponse({'result': 'Good'})

    context = {'logo': logo, 'score': score}

    return render(request, 'imageupload/display_logo_finals.html', context=context)


def display_poster_prelims(request):
    # getting all the objects of Poster .
    score = PosterScoreForm(request.POST or None)
    poster = Poster.objects.filter(roundtype="prelims").order_by('id')

    if request.method == "POST":
        question_id = get_object_or_404(Poster, id=request.POST.get('q_id'))
        Poster.objects.filter(id=question_id.id).update(
            score=request.POST.get('answer'))

        return JsonResponse({'result': 'Good'})

    context = {'poster': poster, 'score': score}

    return render(request, 'imageupload/display_poster_prelims.html', context=context)


def display_poster_finals(request):
    # getting all the objects of Poster .
    score = PosterScoreForm(request.POST or None)
    poster = Poster.objects.filter(roundtype="final").order_by('id')

    if request.method == "POST":
        question_id = get_object_or_404(Poster, id=request.POST.get('q_id'))
        Poster.objects.filter(id=question_id.id).update(
            score=request.POST.get('answer'))

        return JsonResponse({'result': 'Good'})

    context = {'poster': poster, 'score': score}

    return render(request, 'imageupload/display_poster_finals.html', context=context)
