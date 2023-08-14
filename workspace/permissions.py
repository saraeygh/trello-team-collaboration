from rest_framework import permissions
from workspace.models import Workspace

# Mahdieh
class IsProjectAdminOrMemberReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try: 
            pmem = Workspace.objects.get(member=request.user, project=obj)
        except Workspace.DoesNotExist:
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        return pmem.access_level == 2



# Mahdieh
class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        try:
            pmem = Workspace.objects.get(member=request.user, project=obj)
        except Workspace.DoesNotExist:
            return False
        return True