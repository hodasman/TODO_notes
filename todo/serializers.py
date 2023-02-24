from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, TODO
from authapp.serializers import UsersModelSerializer

class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'

class TODOModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    
    class Meta:
        model = TODO
        fields = '__all__'