from typing import Any
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (Workspace,
                     Project,
                     Task,
                     Assignment,
                     Label,
                     LabeledTask,
                     Comment
                     )


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
@admin.register(Workspace)
class Workspace(admin.ModelAdmin):
    list_display = ['name', 'description', 'access_level']
    list_filter = ['name']
    list_per_page = 10


# Mahdieh
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    list_per_page = 10


# Reza
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'updated_at'

    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        label, created = Label.objects.get_or_create(name=obj.name)
        if created:
            return label
        label.save()
        return label


# Reza
@admin.register(LabeledTask)
class LabeledTaskAdmin(admin.ModelAdmin):
    pass


# Reza
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'text', 'soft_delete')
    search_fields = ('user', 'task', 'text')
    list_display_links = ('user', 'task', 'text')
    list_filter = ('soft_delete',)
    date_hierarchy = 'updated_at'

    fieldsets = (
        (None, {
            'fields': (
                'user',
                'task',
                'text',
                )
        }),
    )

    actions = ('soft_delete', 'reactivate')

    @admin.action(description='Logically delete selected comments')
    def soft_delete(self, request, queryset):
        for comment in queryset:
            comment.soft_delete = True
            comment.save()
        return None

    @admin.action(description='Reactivate selected comments')
    def reactivate(self, request, queryset):
        for comment in queryset:
            comment.soft_delete = False
            comment.save()
        return None
