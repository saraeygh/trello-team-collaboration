from django.shortcuts import get_object_or_404
from rest_framework import permissions

from workspace.models import Task, ProjectMember


class HasTaskAccess(permissions.BasePermission):

    def has_permission(self, request, view):
        task_id = view.kwargs.get('task_pk')
        task = get_object_or_404(Task, id=task_id)
        member_id = request.user.id
        has_access = ProjectMember.objects.\
            filter(project_id=task.project.id, member_id=member_id).exists()

        if has_access:
            return True
        return False
