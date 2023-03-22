
from .models import Users
from .serializers import UsersModelSerializer, UsersModelSerializerBase
from rest_framework import mixins, viewsets


class UsersCustomViewSet(mixins.ListModelMixin,
mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UsersModelSerializerBase
        return UsersModelSerializer