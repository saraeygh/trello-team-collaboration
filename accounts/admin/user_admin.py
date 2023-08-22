from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.admin import BaseAdmin
from accounts.models import User, Profile


class ProfileInLine(admin.StackedInline):
    model = Profile
    exclude = ('soft_delete',)


# Reza
@admin.register(User)
class UserAdmin(BaseAdmin, BaseUserAdmin):
    list_select_related = ['profile']
    list_display = ("soft_delete",
                    "username",
                    "email",
                    "full_name",
                    "phone",
                    "gender",
                    "birthdate",
                    "date_joined",
                    )

    list_display_links = ("username", "email", "full_name")
    list_filter = ('soft_delete', 'is_staff')
    ordering = ("-date_joined", "username")
    date_hierarchy = "date_joined"
    readonly_fields = ('date_joined', 'last_login')

    inlines = (ProfileInLine,)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    ),
            },
        ),
    )
