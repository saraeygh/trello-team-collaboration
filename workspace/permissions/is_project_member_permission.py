from rest_framework import permissions

from workspace.models import ProjectMember


# Mahdieh
class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if ProjectMember.objects.filter(member=request.user.id, project=obj).exists():
            return True
        return False
