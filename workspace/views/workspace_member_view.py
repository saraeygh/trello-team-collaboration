from django.shortcuts import get_object_or_404

from workspace.permissions import IsMemberOrReadOnly
from core.views import BaseViewSet
from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import (
    RetrieveWorkspaceMemberSerializer,
    AddWorkspaceMemberSerializer,
    UpdateWorkspaceMemberSerializer
    )


# Mahdieh
class WorkspaceMemberViewSet(BaseViewSet):
    permission_classes = [IsMemberOrReadOnly]

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return WorkspaceMember.objects.select_related("workspace").\
            prefetch_related("member").filter(workspace_id=workspace_id)

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
