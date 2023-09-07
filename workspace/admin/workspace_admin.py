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
        "image",
        'created_at',
        ]
    list_display_links = ("name", "description", "image", "created_at")
    list_filter = ['created_at', 'updated_at']
    inlines = [WorkspaceMemberInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    search_fields = ('name',)
    readonly_fields = ['thumbnil', 'created_at']

    fieldsets = (
        (_("Workspace Information"), {
            'fields': (
                'name',
                'description',
                'created_at',
                'image'
                )
        }),
    )

    def thumbnil(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}"/>')
        return ''

    def get_queryset(self, request):
        workspaces = super().get_queryset(request)
        return workspaces.prefetch_related('member')
