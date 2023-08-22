from rest_framework.viewsets import ModelViewSet

from workspace.models import Workspace
from workspace.serializers import WorkspaceSerializer
from workspace.permisssions import IsProjectAdminOrMemberReadOnly, IsProjectMember

# Mahdieh
class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
