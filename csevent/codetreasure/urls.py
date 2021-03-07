from django.urls import path
from .views import *

app_name = 'codetreasure'


urlpatterns = [
    path('prelims/', prelm_question, name='prelims'),
]
