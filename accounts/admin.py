from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.admin import BaseAdmin
from .models import User


# Reza
@admin.register(User)
class UserAdmin(BaseAdmin, BaseUserAdmin):

    list_display = ("soft_delete",
                    "username",
                    "email",
                    "phone",
                    "get_full_name",
                    "gender",
                    "birthdate",
                    "date_joined",
                    )

    list_display_links = ("username", "email", "get_full_name")
    list_filter = ("soft_delete", "gender", "is_staff", "is_superuser", "groups")
    ordering = ("-date_joined", "username")
    date_hierarchy = "date_joined"
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "email",
                "phone",
                "gender",
                "first_name",
                "last_name",
                "birthdate",
            )
            }),
    )
