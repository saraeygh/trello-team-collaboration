from rest_framework import permissions

from workspace.models import WorkspaceMember


class HasAdminLevel(permissions.BasePermission):

    def has_permission(self, request, view):
        workspace_id = view.kwargs['workspace_pk']
        member_id = request.user.id
        has_access = WorkspaceMember.objects.\
            filter(workspace_id=workspace_id, member_id=member_id, access_level=2).\
            exists()

        if has_access:
            return True
        return False
