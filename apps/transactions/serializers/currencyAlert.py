from rest_framework import serializers

from apps.transactions.models import CurrencyAlert


class CurrencyAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyAlert
        fields = "__all__"
