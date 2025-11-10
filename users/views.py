from rest_framework.generics import ListAPIView
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter


class PaymentListAPI(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PaymentFilter