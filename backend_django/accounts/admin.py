from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model : Account
    list_display = ['email', 'username', 'phone_number', 'is_staff', 'is_active']

admin.site.register(Account, CustomUserAdmin)
