from typing import Any
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from workspace.models import LabeledTask


@admin.register(LabeledTask)
class LabeledTaskAdmin(admin.ModelAdmin):
    list_display = ('label', 'task', 'created_at', 'updated_at')
    search_fields = ('label', 'task')
    date_hierarchy = 'updated_at'
