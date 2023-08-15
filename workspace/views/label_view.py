from rest_framework.viewsets import ModelViewSet

from workspace.models import Label
from workspace.serializers import LabelSerializer


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
