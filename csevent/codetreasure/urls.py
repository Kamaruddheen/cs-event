from django.urls import path
from .views import *

app_name = 'codetreasure'


urlpatterns = [
    #  Prelims
    path('prelims/', prelm_question, name='prelims'),
    path('prelims/status/', prelm_status, name='prelm_status'),
    #  Finals
    # Code Shuffle
    path('finals/codeshuffle/', final_code_shuffle_function,
         name='final_code_shuffle_function'),
    # Spot Error
    path('finals/spoterror/', final_spot_error_function,
         name='final_spot_error_function'),
    # Binary Hunt
    path('finals/binaryhunt/', final_binary_function,
         name='final_binary_function'),
    # Test Final Message
    path('finals/status/', last_binary_question,
         name='last_binary_question'),
    # Cheated Exit Test
    path('text/exit/finals/', finals_exit_test, name="exit_test"),
    path('text/exit/prelims/', prelims_exit_test, name="prelims_exit_test"),
    # Exporting Result
    path('score/finals/', finals_score, name="finals_score"),
    path('score/prelims/', prelims_score, name="prelims_score"),
]
