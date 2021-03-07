from django.urls import path
from .views import *

app_name='codetreasure'

#Define your urls here

urlpatterns=[
    path('prelims/',prelm_question,name='prelims'),
    path('final_code_shuffle/',final_code_shuffle_function,name='final_code_shuffle_function'),
    path('final_binary/',final_binary_function,name='final_binary_function'),
    path('final_spot_error/',final_spot_error_function,name='final_spot_error_function'),
]