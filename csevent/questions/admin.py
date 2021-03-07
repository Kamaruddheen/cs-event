from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(question_model)

class Admin_Stud_Res_CodeTreasure_Prelm(admin.ModelAdmin):
    list_display=['id','student','question','user_answer','status','when']
    search_fields=['student','question']
admin.site.register(Stud_Res_CodeTreasure_Prelm,Admin_Stud_Res_CodeTreasure_Prelm)

class admin_final_answer_relation(admin.ModelAdmin):
    list_display=['id','student','final_code_shuffle_question','final_code_binary_question','final_code_spot_error_question','user_answer','when']
    search_fields=['student','final_code_shuffle_question','final_code_binary_question','final_code_spot_error_question']
admin.site.register(final_code_shuffle)
admin.site.register(final_code_shuffle_relation)
admin.site.register(final_code_binary_question)
admin.site.register(final_code_spot_error_image)
admin.site.register(final_code_spot_error_question)
admin.site.register(final_answer_relation,admin_final_answer_relation)