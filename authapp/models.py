from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models

class Users(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField( max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=False)

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,

    )
    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
