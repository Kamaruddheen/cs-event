from django.contrib import admin

from .models import *


class LogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'status', 'roundtype', 'date_time']
    search_fields = ['student', 'logo']
    ordering = ['roundtype', 'id', ]


admin.site.register(Logo, LogoAdmin)


class PosterAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'status', 'roundtype', 'date_time']
    search_fields = ['student', 'poster', 'roundtype']
    ordering = ['id', 'roundtype']


admin.site.register(Poster, PosterAdmin)
