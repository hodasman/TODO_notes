from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Project, TODO
# from authapp.serializers import UsersModelSerializer

class ProjectModelSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)
    # authors = HyperlinkedRelatedField(view_name='users-detail', many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class TODOModelSerializer(ModelSerializer):
    
    
    class Meta:
        model = TODO
        fields = ('id', 'project', 'text', 'created', 'author', 'is_active')