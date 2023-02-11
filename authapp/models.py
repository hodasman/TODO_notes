from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class Users(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField( max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
