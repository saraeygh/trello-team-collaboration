from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import (
    RetrieveWorkspaceMemberSerializer,
    AddWorkspaceMemberSerializer,
    UpdateWorkspaceMemberSerializer
    )


# Mahdieh
class WorkspaceMemberViewSet(ModelViewSet):

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return WorkspaceMember.objects.\
            filter(workspace_id=workspace_id).\
            prefetch_related("member").\
            select_related("workspace")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveWorkspaceMemberSerializer
        if self.request.method in ('PUT', 'PATCH'):
            return UpdateWorkspaceMemberSerializer
        return AddWorkspaceMemberSerializer

    def get_serializer_context(self):
        workspace = get_object_or_404(
            Workspace,
            id=self.kwargs.get('workspace_pk')
        )
        return {"workspace": workspace}
