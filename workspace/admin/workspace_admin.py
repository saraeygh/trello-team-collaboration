from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import BaseAdmin
from workspace.models import Workspace, WorkspaceMember


# Mahdieh
class WorkspaceMemberInline(admin.TabularInline):
    model = WorkspaceMember

#Mahdieh
@admin.register(Workspace)
class WorkspaceAdmin(BaseAdmin):
    list_display = [
        'soft_delete',
        'id',
        'name',
        'description',
        'created_at',
        ]
    list_display_links = ("id", "name", "description", "created_at")
    list_filter = ['created_at', 'updated_at']
    inlines = [WorkspaceMemberInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (_("Workspace Information"), {
            'fields': (
                'name',
                'description',
                'created_at'
                )
        }),
    )
