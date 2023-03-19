import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from authapp.models import Users
from .views import ProjectModelViewSet, TODOViewSet
from .models import TODO, Project


class TestProjectViewSet(TestCase):

    def setUp(self):
        self.user = Users.objects.create_user('user', 'user@admin.com', 'user123')
        self.admin = Users.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.project = Project.objects.create(name = 'Project5', 
                                         repository = 'http://yandex.by')
        self.data = {'name': 'Project5', 'repository': 'http://yandex.by'}
        self.data_put = {'name': 'Project6', 'repository': 'http://google.com'}

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        force_authenticate(request, self.user)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', self.data, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):

        client = APIClient()
        client.login(username='user', password='user123')
        response = client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_edit_admin(self):

        client = APIClient()
        client.login(username='admin', password='admin123')
        response = client.put(f'/api/projects/{self.project.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(project.name, 'Project6')
        client.logout()

    def tearDown(self):
        pass

class TestTodoViewSet(APITestCase):
    def setUp(self):
        admin = Users.objects.create_superuser('admin', 'admin@admin.com',
                                                'admin123')
        
    def test_get_list(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        todo = mixer.blend(TODO)
        print(todo.project)
        self.client.login(username='admin', password='admin123')
        response = self.client.put(f'/api/todo/{todo.id}/', {'project': todo.project.id, 
            'text': 'new text2', 'is_active': True, 'author': todo.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        pass
