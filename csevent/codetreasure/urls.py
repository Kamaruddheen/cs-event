from django.urls import path
from .views import *

app_name = 'codetreasure'


urlpatterns = [
    #  Prelims
    path('prelims/', prelm_question, name='prelims'),
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
    path('finals/status/', last_question_prelims,
         name='last_question_prelims'),
    path('finals/status/', last_question_final,
         name='last_question_final'), 
    # Exit Test
    path('notallowed/', exit_test, name="exit_test"),

]
