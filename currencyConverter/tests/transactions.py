from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.transactions.models import Transaction
from apps.users.models import User


class TransactionAPITestCase(TestCase):

    def setUp(self):
        # Set up test user and authenticate API client
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass123"
        )
        self.url = reverse("transaction-list")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_transaction(self):
        """
        Test the creation of a valid transaction.
        Ensures that a transaction with correct data is successfully created,
        and that the calculated target amount matches the expected value.
        """
        data = {
            "user": self.user.id,
            "source_currency": "BRL",
            "source_amount": "100.50",
            "target_currency": "USD",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        transaction = Transaction.objects.first()
        expected_target_amount = Decimal(
            Decimal(transaction.source_amount) * Decimal(transaction.conversion_rate)
        ).quantize(Decimal("0.00"), rounding="ROUND_HALF_UP")

        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.source_currency, "BRL")
        self.assertEqual(transaction.source_amount, Decimal("100.50"))
        self.assertEqual(transaction.target_currency, "USD")
        self.assertEqual(transaction.target_amount, expected_target_amount)

    def test_transaction_invalid_currency(self):
        """
        Test that transactions with invalid currency codes are rejected.
        Ensures that providing an unsupported currency returns a 400 response
        and that the correct field error is included in the response.
        """
        data = {
            "user": self.user.id,
            "source_currency": "XYZXX",
            "source_amount": "100.50",
            "target_currency": "USD",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("source_currency", response.data)

        data = {
            "user": self.user.id,
            "source_currency": "XYZ",
            "source_amount": "100.50",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("source_currency", response.data)

    def test_transaction_invalid_amount(self):
        """
        Test that transactions with invalid (negative) amounts are rejected.
        Verifies that submitting a negative source_amount returns a 400 response
        and the appropriate validation error is included.
        """
        data = {
            "user": self.user.id,
            "source_currency": "BRL",
            "source_amount": "-100.50",
            "target_currency": "USD",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("source_amount", response.data)
