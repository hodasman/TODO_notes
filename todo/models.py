from django.db import models
from authapp.models import Users

class Project(models.Model):
    name = models.CharField(max_length=32)
    repository = models.URLField(unique=True)
    authors = models.ManyToManyField(Users)

    def __str__(self):
        return self.name

class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.project} {self.text}'
    
    def close(self, *args):
        self.is_active = False
        self.save()