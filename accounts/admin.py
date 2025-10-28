# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    # Ini akan tampil di daftar user
    list_display = ['username', 'email', 'display_name', 'is_staff']
    
    # Ini untuk menambah 'display_name' saat edit user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('display_name',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)