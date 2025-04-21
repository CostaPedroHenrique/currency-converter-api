from django.db import models

from apps.users.models import User


class Notification(models.Model):
    class NotificationType(models.TextChoices):
        UP = "UP", "Subiu"
        DOWN = "DOWN", "Caiu"
        INFO = "INFO", "Informativo"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(
        max_length=10, choices=NotificationType.choices, default=NotificationType.INFO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} -> {self.user.username}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
