from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from workspace.models import Task, Project
from workspace.serializers import RetrieveTaskSerializer, CreateTaskSerializer


class TaskViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete", "header", "options"]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        
        return Task.objects.filter(soft_delete=False).filter(project_id=project_id)
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrieveTaskSerializer
        return CreateTaskSerializer
    
    def get_serializer_context(self):
        project_id = self.kwargs.get("project_pk")
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error" : "invalid data"})
        return {
            'project': project
        }
    

class TaskViewSetNone(ModelViewSet):
    http_method_names = ["header", "options"]

    queryset = Task.objects.all()
    serializer_class = RetrieveTaskSerializer
