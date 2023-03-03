
from .models import Users
from .serializers import UsersModelSerializer
from rest_framework import mixins, viewsets


class UsersCustomViewSet(mixins.ListModelMixin,
mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer