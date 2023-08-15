from rest_framework.viewsets import ModelViewSet

from workspace.models import LabeledTask
from workspace.serializers import LabeledTaskSerializer


class LabledTaskViewSet(ModelViewSet):
    serializer_class = LabeledTaskSerializer

    def get_queryset(self):
        label_id = self.kwargs.get('label_pk')
        return LabeledTask.objects.filter(label_id=label_id)

    def get_serializer_context(self):
        label_id = self.kwargs.get('label_pk')
        return {'label_id': label_id}
