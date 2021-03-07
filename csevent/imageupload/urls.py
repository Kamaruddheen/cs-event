from django.urls import path
from .views import *


app_name = "imageupload"

urlpatterns = [
    path('webdodger/poster/prelims/', poster_prelims, name='poster_prelims'),
    path('webdodger/poster/finals/', poster_finals, name='poster_finals'),
    path('impreza/logo/prelims/', logo_prelims, name='logo_prelims'),
    path('impreza/logo/finals/', logo_finals, name='logo_finals'),
    path('success/', success, name='success'),
    path('verify/metadata/', verify_meta_img, name="verify_meta"),
]
