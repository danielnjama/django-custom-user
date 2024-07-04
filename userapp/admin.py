from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'phonenumber','activation_code','account_active')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
