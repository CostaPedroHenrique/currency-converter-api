from rest_framework.serializers import ModelSerializer, ValidationError

from apps.transactions.models import Transaction
from apps.transactions.services import ConversionService


class TransactionSerializer(ModelSerializer):
    """
    Serializer for the Transaction model.
    """

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["id", "user", "conversion_rate", "target_amount", "date"]

    def validate_target_currency(self, value):
        source_currency = self.initial_data.get("source_currency")
        if source_currency == value:
            raise ValidationError(
                "Target currency must be different from source currency."
            )
        return value

    def create(self, validated_data):
        """
        Override the create method to include the conversion logic.
        """
        # Extracting the currency conversion details
        source_currency = validated_data.get("source_currency")
        target_currency = validated_data.get("target_currency")
        amount = float(validated_data.get("source_amount"))

        result = ConversionService.convert_currency(
            source_currency, target_currency, amount
        )

        validated_data["target_amount"] = result["converted_amount"]
        validated_data["conversion_rate"] = result["conversion_rate"]
        validated_data["user"] = self.context["request"].user

        return super().create(validated_data)
