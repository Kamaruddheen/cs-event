from django.urls import path
from .views import *


app_name = "imageupload"

urlpatterns = [
    # Test Web Dodger Prelims
    path('webdodger/prelims/', poster_prelims, name='poster_prelims'),
    path('webdodger/finals/', poster_finals, name='poster_finals'),
    # Test Impreza Prelims
    path('impreza/prelims/', logo_prelims, name='logo_prelims'),
    path('impreza/finals/', logo_finals, name='logo_finals'),
    # Finished Status
    path('success/', success, name='success'),
    path('verify/metadata/', verify_meta_img, name="verify_meta"),
    # Logo Score
    path('impreza/prelims/result/score/', display_logo_prelims,
         name='display_logo_prelims'),
    path('impreza/finals/result/score/', display_logo_finals,
         name='display_logo_finals'),
    # Poster Score  
    # Display Logo & Poster
    path('webdodger/prelims/result/score/', display_poster_prelims,
         name='display_poster_prelims'),
    path('webdodger/finals/result/score/', display_poster_finals,
         name='display_poster_finals'),
]
