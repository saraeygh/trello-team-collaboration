from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import BaseAdmin
from workspace.models import Comment


# Reza
@admin.register(Comment)
class CommentAdmin(BaseAdmin):
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
