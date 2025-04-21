from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet, mixins

from apps.transactions.models.transaction import Transaction
from apps.transactions.serializers.transaction import TransactionSerializer


class TransactionViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    """
    ViewSet for the Transaction model.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "user": ["exact"],
        "date": ["exact", "range"],
    }

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied(
                "You do not have permission to delete this transaction."
            )
        return super().destroy(request, *args, **kwargs)
