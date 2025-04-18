from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that uses username and email as unique identifiers.
    """

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = "User"
