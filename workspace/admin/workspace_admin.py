from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import BaseAdmin
from workspace.models import Workspace


#Mahdieh
@admin.register(Workspace)
class WorkspaceAdmin(BaseAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'member',
        'access_level',
        'created_at',
        ]
    list_filter = ['created_at', 'access_level', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ('-created_at', 'access_level')
    search_fields = ('name', 'access_level',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (_("Workspace Information"), {
            'fields': (
                'name',
                'description',
                'member',
                'access_level',
                'created_at'
                )
        }),
    )
