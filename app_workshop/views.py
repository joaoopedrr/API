from app_workshop.models import Todo
from app_workshop.serializers import TodoSerializer


from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer




