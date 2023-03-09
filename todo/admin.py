from django.contrib import admin
from todo.models import TODO, Project


@admin.register(TODO)
class CustomTODOAdmin(admin.ModelAdmin):
    list_display = ["id", "project", "text", "author", "is_active", "created"]
    ordering = ["-id"]

@admin.register(Project)
class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "repository"]
    ordering = ["-id"]
