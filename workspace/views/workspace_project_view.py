from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from workspace.models import Project, Workspace
from workspace.serializers import RetrieveProjectSerializer, CreateProjectSerializer


class WorkspaceProjectViewSet(ModelViewSet):

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return Project.objects.filter(soft_delete=False).filter(workspace_id=workspace_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveProjectSerializer
        return CreateProjectSerializer

    def get_serializer_context(self):
        id = self.kwargs.get('workspace_pk')
        workspace = get_object_or_404(
            Workspace,
            id=id
        )
        return {"workspace": workspace}
