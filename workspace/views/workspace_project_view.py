from datetime import datetime
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from workspace.models import Project, Workspace
from workspace.serializers import WorkspaceProjectSerializer


class WorkspaceProjectViewSet(ModelViewSet):

    serializer_class = WorkspaceProjectSerializer

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_pk')
        return Project.objects.filter(soft_delete=False).filter(workspace_id=workspace_id)

    def create(self, request, *args, **kwargs):
        name = self.request.data.get('name')
        if name is None or name == '':
            return Response(
                {
                    "Error": "Invalid name"
                }, status=status.HTTP_400_BAD_REQUEST
            )

        description = self.request.data.get('description')
        deadline = self.request.data.get('deadline')
        workspace = self.kwargs.get('workspace_pk')
        member = self.request.user

        try:
            workspace = Workspace.objects.get(id=workspace)
        except Workspace.DoesNotExist:
            return Response(
                {"Error": "Workspace does not exist."}
            )

        project = Project.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            workspace=workspace,
        )
        serializer = WorkspaceProjectSerializer(project)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        name = self.request.data.get('name')
        description = self.request.data.get('description')
        deadline = self.request.data.get('deadline')
        project_id = self.kwargs.get('pk')

        if name is None or name == '':
            return Response(
                {
                    "Error": "Invalid name"
                }, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            deadline = datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            return Response(
                {
                    "Error": "Invalid DateTime format"
                }
            )

        try:
            project = Project.objects.get(id=project_id)
        except Workspace.DoesNotExist:
            return Response(
                {"Error": "Project does not exist."}
            )

        project.name = name
        project.description = description
        project.deadline = deadline
        project.save()

        serializer = WorkspaceProjectSerializer(project)
        return Response(serializer.data)
