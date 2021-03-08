from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html',context={'minheight':'min-height: 100vh;'})