from django.contrib import admin
from .models import *


class question_model_Admin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_A',
                    'option_B', 'option_C', 'option_D', 'correct_option']
    search_fields = ['id', 'question']
    ordering = ['id']


admin.site.register(question_model, question_model_Admin)


class Admin_Stud_Res_CodeTreasure_Prelm(admin.ModelAdmin):
    list_display = ['id', 'student', 'question',
                    'user_answer', 'status', 'when']
    search_fields = ['id', 'student']
    ordering = ['id']


admin.site.register(Stud_Res_CodeTreasure_Prelm,
                    Admin_Stud_Res_CodeTreasure_Prelm)
