from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'phonenumber', 'location')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
