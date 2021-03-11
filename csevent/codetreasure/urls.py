from django.urls import path
from .views import *

app_name = 'codetreasure'


urlpatterns = [
    #  Prelims
    path('prelims/', prelm_question, name='prelims'),
    path('prelims/status/', last_question_prelims, name='last_question_prelims'),
    path('final/status/',last_question_final,name='last_question_final'),
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
    #cheated url path :
    path('cheated/prelims/',exit_test_preliminary,name='exit_test_preliminary'),
    path('cheated/final/',exit_test_final,name='exit_test_final'),
]
