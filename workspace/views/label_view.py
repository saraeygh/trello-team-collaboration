from rest_framework.viewsets import ModelViewSet

from workspace.models import Label, LabeledTask
from workspace.serializers import LabelSerializer, LabeledTaskSerializer


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabledTaskViewSet(ModelViewSet):
    serializer_class = LabeledTaskSerializer

    def get_queryset(self):
        return LabeledTask.objects.filter(label_id=self.kwargs['label_pk'])

    def get_serializer_context(self):
        return {'label_id': self.kwargs['label_pk']}
