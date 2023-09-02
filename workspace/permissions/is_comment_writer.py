from django.shortcuts import get_object_or_404
from rest_framework import permissions

from workspace.models import Task, ProjectMember, Comment


class IsCommentWriter(permissions.BasePermission):

    def has_permission(self, request, view):
        comment_id = view.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:
            return True
        return False
