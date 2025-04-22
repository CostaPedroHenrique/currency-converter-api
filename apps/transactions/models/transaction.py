from django.core.validators import MinValueValidator
from django.db import models

from apps.users.models import User

SUPPORTED_CURRENCIES = (
    ("BRL", "Brazilian Real"),
    ("USD", "US Dollar"),
    ("EUR", "Euro"),
    ("JPY", "Japanese Yen"),
)


class Transaction(models.Model):
    """
    Model representing a currency conversion transaction.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_currency = models.CharField(max_length=3, choices=SUPPORTED_CURRENCIES)
    source_amount = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)]
    )
    target_currency = models.CharField(max_length=3, choices=SUPPORTED_CURRENCIES)
    target_amount = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)]
    )
    conversion_rate = models.DecimalField(max_digits=12, decimal_places=6)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username}: "
            f"{self.source_amount} {self.source_currency} → {self.target_currency}"
        )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["-date"]
        app_label = "transactions"
