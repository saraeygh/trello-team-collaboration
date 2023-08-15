from rest_framework.viewsets import ModelViewSet

from workspace.models import Workspace
from workspace.serializers import WorkspaceSerializer


# Mahdieh
class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
