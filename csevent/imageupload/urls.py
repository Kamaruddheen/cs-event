from django.urls import path
from .views import *


app_name = "imageupload"

urlpatterns = [
    path('webdoger/poster/prelims/', poster_prelims, name='poster_prelims'),
    path('webdoger/poster/finals/', poster_finals, name='poster_finals'),
    path('impreza/logo/', logo, name='logo'),
    path('success/', success, name='success'),
]
