from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import TODO, Project
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .filters import ProjectFilter


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter

class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_fields = ['id', 'author']
    

    def destroy(self, request, pk=None):
        todo = get_object_or_404(TODO, pk=pk)
        todo.close()
        return Response(status=200)
