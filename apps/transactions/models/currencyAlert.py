from django.conf import settings
from django.db import models

SUPPORTED_CURRENCIES = (
    ("BRL", "Brazilian Real"),
    ("USD", "US Dollar"),
    ("EUR", "Euro"),
    ("JPY", "Japanese Yen"),
)


class CurrencyAlert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    source_currency = models.CharField(max_length=3, choices=SUPPORTED_CURRENCIES)
    target_currency = models.CharField(max_length=3, choices=SUPPORTED_CURRENCIES)
    base_rate = models.DecimalField(max_digits=12, decimal_places=6)
    variation_threshold = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Percentage variation to trigger notification (e.g., 5.00 = 5%)",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username}: "
            f"Alert for {self.source_currency} to {self.target_currency} "
            f"at {self.base_rate} ({self.threshold_type})"
        )

    class Meta:
        verbose_name = "Currency Alert"
        verbose_name_plural = "Currency Alerts"
        ordering = ["-created_at"]
        unique_together = (("user", "source_currency", "target_currency"),)
