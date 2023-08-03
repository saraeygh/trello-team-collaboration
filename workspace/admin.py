from django.contrib import admin
from .models import Task, Assignment
from django.utils.translation import gettext_lazy as _


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "due_date", "status", "priority")
    list_filter = ("status", "priority", "assigned_to")
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
                'priority'
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


class AssignmentModelAdmin(admin.ModelAdmin):
    list_display = ('task', 'assigned_to', 'assigned_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = (
        'task__title',
        'assigned_to__username',
        'assigned_by__username'
        )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    readonly_fields = ('created_at',)

    fieldsets = (
        (_("Assignment Information"), {
            'fields': (
                'task',
                'assigned_to',
                'assigned_by',
                'created_at'
                )
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('task', 'assigned_to', 'assigned_by')


admin.site.register(Task, TaskModelAdmin)
admin.site.register(Assignment, AssignmentModelAdmin)
