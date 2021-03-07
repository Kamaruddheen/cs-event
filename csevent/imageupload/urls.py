from django.urls import path
from .views import *


app_name = "imageupload"

urlpatterns = [
    path('webdodger/poster/prelims/', poster_prelims, name='poster_prelims'),
    path('webdodger/poster/finals/', poster_finals, name='poster_finals'),
    path('impreza/logo/', logo, name='logo'),
    path('success/', success, name='success'),
]
