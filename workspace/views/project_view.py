from rest_framework.viewsets import ModelViewSet

from workspace.models import Project
from workspace.serializers import RetrieveProjectSerializer


class ProjectViewSet(ModelViewSet):
    http_method_names = ('header', 'options')
    queryset = Project.objects.all()
    serializer_class = RetrieveProjectSerializer
