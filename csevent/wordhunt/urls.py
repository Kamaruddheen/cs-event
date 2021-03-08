from django.urls import path
from .views import *

app_name = "wordhunt"

urlpatterns = [
    path('prelims/sectionA/', question_prelims_sectionA, name="prelims"),
    path('prelims/sectionB/', question_prelims_sectionB, name="prelimsB"),
    path('prelims/submit_answer/', answer_submit, name="answer_submit_prelims"),
    path('finals/sectionA/', question_finals_sectionA, name="finals"),
    path('finals/sectionB/', question_finals_sectionB, name="finalsB"),
    # path('prelims/submit_answer/', answer_submit, name="answer_submit_prelims"),
]
