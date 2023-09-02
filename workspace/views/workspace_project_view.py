from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from workspace.models import Project, Workspace
from workspace.serializers import RetrieveProjectSerializer, CreateProjectSerializer


class WorkspaceProjectViewSet(ModelViewSet):

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return Project.objects.\
            filter(Q(soft_delete=False) & Q(workspace_id=workspace_id)).\
            select_related("workspace").\
            prefetch_related("member")

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
