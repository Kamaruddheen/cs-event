from django.contrib import admin

from .models import *


class LogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'score',
                    'status', 'roundtype', 'date_time']
    search_fields = ['student', 'logo']
    ordering = ['-roundtype', '-score', ]


admin.site.register(Logo, LogoAdmin)


class PosterAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'score',
                    'status', 'roundtype', 'date_time']
    search_fields = ['student', 'poster', 'roundtype']
    ordering = ['-roundtype', '-score']


admin.site.register(Poster, PosterAdmin)
