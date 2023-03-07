from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from authapp import models


@admin.register(models.Users)
class CustomUserAdmin(UserAdmin):
    list_display = ["id", "username", "email", "is_active"]
    ordering = ["-id"]

    
