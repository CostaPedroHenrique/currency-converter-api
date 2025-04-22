from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.notifications.models import Notification

User = get_user_model()


class NotificationAPITest(TestCase):
    def setUp(self):
        # Set up test user and authenticate API client
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpass",
            username="testuser",
        )
        self.client.force_authenticate(user=self.user)

    def test_list_notifications(self):
        """
        Test retrieving notifications for the authenticated user.
        Ensures that a created notification is returned with correct fields
        and that the response status is HTTP 200.
        """
        Notification.objects.create(
            user=self.user,
            title="Test Notification",
            message="Test message",
            type="INFO",
        )

        response = self.client.get("/api/notifications/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Test Notification")
        self.assertEqual(response.data["results"][0]["message"], "Test message")
        self.assertEqual(response.data["results"][0]["type"], "INFO")
        self.assertEqual(response.data["results"][0]["is_read"], False)
        self.assertEqual(response.data["results"][0]["user"], self.user.id)
