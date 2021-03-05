from django.urls import path
from .views import *

app_name = "wordhunt"

urlpatterns = [
    path('prelims/', question_prelims_view, name="prelims")
]
