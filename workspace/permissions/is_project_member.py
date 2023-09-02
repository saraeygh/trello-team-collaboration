from rest_framework import permissions

from workspace.models import ProjectMember


class IsProjectMemebr(permissions.BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        member_id = request.user.id
        is_member = ProjectMember.objects.\
            filter(project_id=project_id, member_id=member_id).exists()

        if is_member:
            return True
        return False
