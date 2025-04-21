from django.core.exceptions import PermissionDenied
from rest_framework import viewsets

from apps.transactions.models import CurrencyAlert
from apps.transactions.serializers import CurrencyAlertSerializer


class CurrencyAlertViewSet(viewsets.ModelViewSet):
    queryset = CurrencyAlert.objects.all()
    serializer_class = CurrencyAlertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return CurrencyAlert.objects.filter(user=user)

    def get_object(self):
        user = self.request.user
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs["pk"])
        if obj.user != user:
            raise PermissionDenied("You do not have permission to access this object.")
        return obj
