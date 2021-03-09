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
    list_display = ('first_name', 'user_type', 'email', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('email', 'user_type', )


admin.site.register(StudentModel)

admin.site.register(prelim_test)
admin.site.register(final_test)
admin.site.register(test_timings)
