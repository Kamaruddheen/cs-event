from django.contrib import admin
from .models import *


class WordhuntAdmin(admin.ModelAdmin):
    list_display = ['id', 'section', 'roundtype']
    search_fields = ['id']
    ordering = ['id', 'roundtype']


admin.site.register(Wordhunt, WordhuntAdmin)


class WordhuntImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id', 'image']
    ordering = ['id', ]


admin.site.register(Images, WordhuntImagesAdmin)


class Stud_Res_WordHuntAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'question',
                    'roundtype', 'status', 'date_time']
    search_fields = ['id', ]
    ordering = ['student', 'question', '-date_time']


admin.site.register(Stud_Res_WordHunt, Stud_Res_WordHuntAdmin)


class Score_wordhuntModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'roundtype', 'score']
    search_fields = ['id', ]
    ordering = ['student', 'roundtype', '-score']


admin.site.register(Score_wordhuntModel, Score_wordhuntModelAdmin)
