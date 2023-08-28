from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from workspace.models import Workspace, WorkspaceMember
from workspace.serializers import WorkspaceMemberSerializer, WorkspaceSerializer
from workspace.permisssions import IsProjectAdminOrMemberReadOnly, IsProjectMember


# Mahdieh
class WorkspaceViewSet(ModelViewSet):

    serializer_class = WorkspaceSerializer
    # permission_classes = [IsProjectMember]

    def get_queryset(self):
        return Workspace.objects.filter(soft_delete=False).filter(member=self.request.user.id)

    def create(self, request, *args, **kwargs):
        member = self.request.user
        name = self.request.data.get('name')
        description = self.request.data.get('description')

        if name is None or name == "":
            return Response(
                {'Error': "Please insert a name."}
                )

        workspace = Workspace.objects.create(
            name=name,
            description=description
            )
        serializer = WorkspaceSerializer(instance=workspace)

        WorkspaceMember.objects.create(
            workspace=workspace,
            member=member,
            access_level=2,
        )

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        name = self.request.data.get('name')
        description = self.request.data.get('description')

        if name is None or name == "":
            return Response(
                {'Error': "Please insert a name."}
                )
        try:
            workspace = Workspace.objects.get(id=self.kwargs['pk'])
            workspace.name = name
            workspace.description = description
            workspace.save()
            serializer = WorkspaceSerializer(workspace)
            return Response(serializer.data)

        except Workspace.DoesNotExist:
            return Response(
                {"Error": "Not found"}
            )

    def destroy(self, request, *args, **kwargs):

        try:
            workspace = Workspace.objects.get(id=self.kwargs['pk'])
            workspace.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Workspace.DoesNotExist:
            return Response(
                {"Error": "Not found"}
            )
