from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfile


# Reza
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    exclude = ('soft_delete',)


# Reza
@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ("username",
                    "soft_delete",
                    "email",
                    "get_full_name",
                    "date_joined"
                    )

    list_display_links = ("username", "email", "get_full_name")
    list_filter = ("soft_delete", "is_staff", "is_superuser", "groups")
    ordering = ("username", "-date_joined")
    date_hierarchy = "date_joined"
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    )
    actions = ('soft_delete', 'reactivate')

    @admin.action(description='Logically delete selected users')
    def soft_delete(self, request, queryset):
        for user in queryset:
            user.soft_delete = True
            user.save()
        return None

    @admin.action(description='Reactivate selected users')
    def reactivate(self, request, queryset):
        for user in queryset:
            user.soft_delete = False
            user.save()
        return None

    inlines = (UserProfileInLine,)
