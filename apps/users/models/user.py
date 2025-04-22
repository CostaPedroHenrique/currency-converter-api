from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"


@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    """
    Create a notification for the user when a new user is created.
    """
    from apps.notifications.models import Notification

    if created:
        Notification.objects.create(
            user=instance,
            title="Welcome to our platform!",
            message="Thank you for signing up. We hope you enjoy your experience.",
            type="INFO",
        )
