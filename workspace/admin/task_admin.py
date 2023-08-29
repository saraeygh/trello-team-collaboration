from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import BaseAdmin
from workspace.models import Task


# Hossein
@admin.register(Task)
class TaskModelAdmin(BaseAdmin):
    list_display = (
        "id",
        "title",
        "start_date",
        "due_date",
        "status",
        "priority",
        "project",
        "soft_delete"
        )
    list_display_links = (
        "title",
        "start_date",
        "due_date",
        "status",
        "priority",
        "project",
        )
    list_filter = ("status", "priority")
    search_fields = ("title", "description", "assigned_to__username")
    date_hierarchy = "due_date"
    ordering = ("-due_date",)

    fieldsets = (
        (_("Task Information"), {
            'fields': (
                'title',
                'description',
                'due_date',
                'status',
                'priority',
                'project',
                )
        }),
        (_("Date and Time"), {
            'fields': (
                'start_date',
                'end_date'
                ),
            'classes': (
                'collapse',
                ),
        }),
    )
    readonly_fields = (
        'start_date',
        )
