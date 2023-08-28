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

    #permission_classes = [IsProjectMember]

    def get_queryset(self):
        return WorkspaceMember.objects.filter(member=self.request.user.id).\
            filter(soft_delete=False)
    
    def get_serializer_class(self):
        #workspace_id =self.kwargs.get('pk')

        if self.request.method == 'GET':
            return WorkspaceMemberSerializer
        
        elif self.request.method == 'POST':
            return WorkspaceSerializer
        
        elif self.request.method in ['PUT', 'PATCH']:
            return WorkspaceSerializer
        
    def create(self, request, *args, **kwargs):
        member = self.request.user
        name = self.request.data.get('name')
        description = self.request.data.get('descrition')
        if name is None or name == "":
            return Response ({'error':"insert name"})

        workspace = Workspace.objects.create(
            name=name, 
            description=description
            )
        workspacemember = WorkspaceMember.objects.create(
            workspace=workspace,
            member=member,
            access_level=2,
        )
        serializer = WorkspaceSerializer(instance=workspace)
        return Response(serializer.data)

        
        