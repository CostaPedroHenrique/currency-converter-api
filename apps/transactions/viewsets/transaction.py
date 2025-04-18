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

    def get_queryset(self):
        """
        Returns only transactions of the authenticated user.
        """
        return self.queryset.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied(
                "Você não tem permissão para deletar esta transação."
            )
        return super().destroy(request, *args, **kwargs)
