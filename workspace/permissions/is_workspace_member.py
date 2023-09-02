from rest_framework import permissions

from workspace.models import WorkspaceMember


class IsWorkspaceMemebr(permissions.BasePermission):

    def has_permission(self, request, view):
        workspace_id = view.kwargs['workspace_pk']
        member_id = request.user.id
        is_member = WorkspaceMember.objects.\
            filter(workspace_id=workspace_id, member_id=member_id).exists()

        if is_member:
            return True
        return False
