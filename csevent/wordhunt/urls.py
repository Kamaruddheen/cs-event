from django.urls import path
from .views import *

app_name = "wordhunt"

urlpatterns = [
    # Reteriving Q/A for Prelims & Finals
    path('prelims/sectionA/', question_prelims_sectionA, name="prelims"),
    path('prelims/sectionB/', question_prelims_sectionB, name="prelimsB"),
    path('finals/sectionA/', question_finals_sectionA, name="finals"),
    path('finals/sectionB/', question_finals_sectionB, name="finalsB"),
    # Answer Submission URl for Prelims & Finals
    path('prelims/submit_answer/', answer_submit, name="answer_submit_prelims"),
    # Cheated Prelims & Finals
    path('text/exit/', exit_test, name="exit_test"),
    # Test submitted
    path('finished_test/<int:id>/', finished_test, name="finished_test"),
]
