from rest_framework.viewsets import ModelViewSet

from core.views import BaseViewSet
from workspace.models import Workspace, WorkspaceImage
from workspace.serializers import (
    CreateWorkspaceSerializer,
    RetrieveWorkspaceSerializer,
    WorkspaceImageSerializer,
)


# Mahdieh
class WorkspaceViewSet(BaseViewSet):

    def get_queryset(self):
        return Workspace.objects.prefetch_related("member").\
            filter(soft_delete=False).filter(member=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveWorkspaceSerializer
        return CreateWorkspaceSerializer


class WorkspaceImageViewSet(ModelViewSet):
    serializer_class = WorkspaceImageSerializer

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}
    
    def get_queryset(self):
        return WorkspaceImage.objects.filter(
            workspace_id=self.kwargs['workspace_pk'])
    