from rest_framework import viewsets
from .models import ToDo_List
from .serializer import TodolistSerializer


class TodolistApi(viewsets.ModelViewSet):
    queryset=ToDo_List.objects.all()
    serializer_class=TodolistSerializer
        