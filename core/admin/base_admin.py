from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    actions = ('soft_delete', 'reactivate')

    @admin.action(description='Deactive')
    def soft_delete(self, request, queryset):
        for item in queryset:
            item.soft_delete = True
            item.save()
        return None

    @admin.action(description='Reactivate')
    def reactivate(self, request, queryset):
        for item in queryset:
            item.soft_delete = False
            item.save()
        return None
