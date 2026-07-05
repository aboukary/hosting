from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "matricule",
        "last_name",
        "first_name",
        "department",
        "level",
    )

    search_fields = (
        "matricule",
        "last_name",
        "first_name",
    )

    list_filter = (
        "department",
        "level",
        "gender",
    )