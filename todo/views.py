from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import TODO, Project
from .serializers import ProjectModelSerializer, TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TODOViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request):
        todos = TODO.objects.all()
        serializer = TODOModelSerializer(todos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        todo = get_object_or_404(TODO, pk=pk)
        serializer = TODOModelSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def create(self, request):
        pass

    def destroy(self, request, pk=None):
        todo = get_object_or_404(TODO, pk=pk)
        todo.close()
