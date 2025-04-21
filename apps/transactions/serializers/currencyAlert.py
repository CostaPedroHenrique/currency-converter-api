from rest_framework.serializers import ModelSerializer, ValidationError

from apps.transactions.models import CurrencyAlert


class CurrencyAlertSerializer(ModelSerializer):
    class Meta:
        model = CurrencyAlert
        fields = "__all__"

    def validate_target_currency(self, value):
        source_currency = self.initial_data.get("source_currency")
        if source_currency == value:
            raise ValidationError(
                "Target currency must be different from source currency."
            )
        return value
