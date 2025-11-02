from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lessons")
    ordering_fields = ("date", "payment_method")


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
