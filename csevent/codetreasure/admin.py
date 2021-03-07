from django.contrib import admin
from .models import *


admin.site.register(question_model)


class Admin_Stud_Res_CodeTreasure_Prelm(admin.ModelAdmin):
    list_display = ['id', 'student', 'question',
                    'user_answer', 'status', 'when']
    search_fields = ['id', 'student']


admin.site.register(Stud_Res_CodeTreasure_Prelm,
                    Admin_Stud_Res_CodeTreasure_Prelm)
