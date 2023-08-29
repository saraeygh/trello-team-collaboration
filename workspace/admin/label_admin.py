from typing import Any
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from workspace.models import Label


# Reza
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'used_count', 'created_at', 'updated_at')
    list_display_links = ('name', 'used_count', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'updated_at'

    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        label, created = Label.objects.get_or_create(name=obj.name)
        return label
