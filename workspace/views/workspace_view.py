from core.views import BaseViewSet
from workspace.models import Workspace
from workspace.serializers import (
    CreateWorkspaceSerializer,
    RetrieveWorkspaceSerializer
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
