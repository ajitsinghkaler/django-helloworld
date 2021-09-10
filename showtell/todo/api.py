from rest_framework.viewsets import ModelViewSet
from .serialisers import TodoSerializer
from .models import TodoModel

class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer