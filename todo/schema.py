import graphene
from graphene_django import DjangoObjectType
from todo.models import Project, TODO
from authapp.models import Users

class TodoType (DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType (DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class UserType (DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'

    
class Query(graphene.ObjectType):
    all_todo = graphene.List(TodoType)
    all_project = graphene.List(ProjectType)
    all_user = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_all_todo(root, info):
        return TODO.objects.all()
    
    def resolve_all_project(root, info):
        return Project.objects.all()
    
    def resolve_all_user(root, info):
        return Users.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExist:
            return None
    
schema = graphene.Schema(query=Query)

