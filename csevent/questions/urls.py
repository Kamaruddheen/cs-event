from django.urls import path
from .views import *
app_name='question'

#Define your urls here
urlpatterns=[
    path('prelm_question/',prelm_question,name='prelm_question'),
]