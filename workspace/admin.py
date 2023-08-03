from django.contrib import admin
from workspace import models


# Mahdieh
@admin.register(models.Workspace)
class Workspace(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_admin']
    list_editable = ['description', 'name']
    list_filter = ['name']
    list_per_page = 10

    @admin.display(ordering='access_level')
    def is_admin(self, project):
        if Workspace.access_level == 2:
            return 'admin'
        return 'member'


# Mahdieh
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['member', 'name', 'color']
    list_filter = ['name', 'owner']
    list_per_page = 10

