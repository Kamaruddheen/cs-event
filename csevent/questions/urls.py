from django.urls import path
from .views import *
app_name='codetreasure'

#Define your urls here
urlpatterns=[
    path('prelims/',prelm_question,name='prelims'),
]