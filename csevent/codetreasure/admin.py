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


class Admin_final_code_shuffle(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id', 'image']
    ordering = ['id']


admin.site.register(final_code_shuffle, Admin_final_code_shuffle)
admin.site.register(final_code_shuffle_relation)


class Admin_final_code_binary_question(admin.ModelAdmin):
    list_display = ['id', 'question']
    search_fields = ['id', 'question']
    ordering = ['id']


admin.site.register(final_code_binary_question,
                    Admin_final_code_binary_question)


class Admin_final_code_spot_error_image(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id', 'image']
    ordering = ['id']


admin.site.register(final_code_spot_error_image,
                    Admin_final_code_spot_error_image)
admin.site.register(final_code_spot_error_question)


class admin_final_answer_relation(admin.ModelAdmin):
    list_display = ['id', 'student', 'final_code_shuffle_question',
                    'final_code_binary_question', 'final_code_spot_error_question', 'user_answer', 'when']
    search_fields = ['student', 'final_code_shuffle_question',
                     'final_code_binary_question', 'final_code_spot_error_question']


admin.site.register(final_answer_relation, admin_final_answer_relation)
