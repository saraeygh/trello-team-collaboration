from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import BaseAdmin
from workspace.models import Project, ProjectMember


# Mahdieh
class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember


# Mahdieh
@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    list_display = ['id', 'name', 'description', 'workspace']
    readonly_fields = ('created_at', 'deadline') 
    inlines = [ProjectMemberInline]
    list_filter = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    fieldsets = (
        (_("Project Information"), {
            'fields': (
                'name',
                'description',
                'workspace',
                )
        }),
        (_("Date and Time"), {
            'fields': (
                'created_at',
                'deadline'
                ),
            'classes': (
                'collapse',
                ),
        }),
    )