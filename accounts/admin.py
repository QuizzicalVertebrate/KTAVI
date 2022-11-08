from django.contrib import admin
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    class Meta():
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ['email', 'username']



admin.site.register(CustomUser, CustomUserAdmin)