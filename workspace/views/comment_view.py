from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from workspace.models import Comment, Task
from workspace.permissions import HasTaskAccess, IsCommentWriter
from workspace.serializers import (
    CreateCommentSerializer,
    RetrieveCommentSerializer
    )


# Reza
@extend_schema(tags=["Comments"])
class CommentViewSet(ModelViewSet):
    serializer_class = RetrieveCommentSerializer
    permission_classes = [IsAuthenticated, HasTaskAccess]

    def get_permissions(self):
        if self.request.method in ['GET', 'POST', 'HEADER', 'OPTIONS']:
            return [IsAuthenticated(), HasTaskAccess()]
        return [IsAuthenticated(), HasTaskAccess(), IsCommentWriter()]

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return Comment.objects.\
            filter(Q(soft_delete=False) & Q(task_id=task_id)).\
            select_related('user').\
            select_related('task')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveCommentSerializer
        return CreateCommentSerializer

    def get_serializer_context(self):
        user = self.request.user
        task = get_object_or_404(Task, id=self.kwargs.get('task_pk'))
        return {
            "user": user,
            "task": task
            }
