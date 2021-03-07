from django.contrib import admin

from .models import *


class LogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'status', 'date_time']
    search_fields = ['student', 'logo']


admin.site.register(Logo, LogoAdmin)


class PosterAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'status', 'roundtype', 'date_time']
    search_fields = ['student', 'poster', 'roundtype']


admin.site.register(Poster, PosterAdmin)
