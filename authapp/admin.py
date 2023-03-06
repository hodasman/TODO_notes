from django.contrib import admin

from authapp import models


@admin.register(models.Users)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active"]
    ordering = ["-id"]
