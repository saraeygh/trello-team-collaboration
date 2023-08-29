from rest_framework.viewsets import ModelViewSet

from workspace.serializers import (
    CreateWorkspaceSerializer,
    RetrieveWorkspaceSerializer
)
from workspace.models import Workspace


# Mahdieh
class WorkspaceViewSet(ModelViewSet):

    def get_queryset(self):
        return Workspace.objects.prefetch_related("member").filter(soft_delete=False).filter(member=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveWorkspaceSerializer
        return CreateWorkspaceSerializer
