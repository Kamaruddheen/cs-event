from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'user_type', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'mobile', 'user_type', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'first_name', 'user_type', 'email', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('email', 'user_type', )


admin.site.register(StudentModel)


class prelim_test_admin(admin.ModelAdmin):
    list_display = ['id', 'Student', 'event', 'test_status', 'attended']
    search_fields = ['id', 'test_status', 'event']
    ordering = ['Student', 'event']


admin.site.register(prelim_test, prelim_test_admin)


class final_test_admin(admin.ModelAdmin):
    list_display = ['id', 'student', 'event', 'test_status', 'attended']
    search_fields = ['id', 'test_status', 'event']
    ordering = ['student', 'event']


admin.site.register(final_test, final_test_admin)


class test_timings_admin(admin.ModelAdmin):
    list_display = ['id', 'event', 'round_type', 'start', 'end', ]
    search_fields = ['id', 'event', 'round_type']
    ordering = ['-id', ]


admin.site.register(test_timings, test_timings_admin)
