from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ProjectMember, Workspace, Project, Task, Assignment, WorkspaceMember


# Hossein
@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "due_date", "status", "priority", "project")
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
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('task', 'assigned_to', 'assigned_by')


# Mahdieh
@admin.register(WorkspaceMember)
class WorkspaceMember(admin.ModelAdmin):
    list_display = ['created_at', 'access_level']
#    list_filter = ['name']
    list_per_page = 10

# Mahdieh
@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ['members', 'created_at']
    list_filter = ['created_at']
    list_per_page = 10

