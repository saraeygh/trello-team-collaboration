from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from workspace.models import Assignment


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
