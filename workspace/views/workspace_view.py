from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from workspace.serializers import (
    CreateWorkspaceSerializer,
    RetrieveWorkspaceSerializer
)
from workspace.models import Workspace, WorkspaceMember


# Mahdieh
class WorkspaceViewSet(ModelViewSet):

    def get_queryset(self):
        return Workspace.objects.\
            filter(Q(soft_delete=False) & Q(member=self.request.user)).\
            prefetch_related("member")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveWorkspaceSerializer
        return CreateWorkspaceSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        member = get_object_or_404(
            WorkspaceMember,
            workspace_id=instance.id,
            member_id=request.user.id
        )

        if member.access_level == 2:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {"Error": "Only admins can delete workspaces."},
            status=status.HTTP_403_FORBIDDEN
            )
