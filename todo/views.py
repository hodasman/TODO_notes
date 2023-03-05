from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import TODO, Project
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .filters import ProjectFilter
from rest_framework.pagination import LimitOffsetPagination

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination

class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_fields = ['id']
    pagination_class = TODOLimitOffsetPagination
    

    def destroy(self, request, pk=None):
        todo = get_object_or_404(TODO, pk=pk)
        todo.close()
        return Response(status=200)
