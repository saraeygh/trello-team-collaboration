from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Workspace, Project, Task, Assignment


# Hossein
@admin.register(Task)
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


# Hossein
@admin.register(Assignment)
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


# Mahdieh
@admin.register(Workspace)
class Workspace(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_admin']
    list_editable = ['description', 'name']
    list_filter = ['name']
    list_per_page = 10

    @admin.display(ordering='access_level')
    def is_admin(self, project):
        if Workspace.access_level == 2:
            return 'admin'
        return 'member'


# Mahdieh
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['member', 'name', 'color']
    list_filter = ['name', 'owner']
    list_per_page = 10
