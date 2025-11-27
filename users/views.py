from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from users.models import Payments, CustomUser
from users.permissions import IsOwner
from users.serializers import PaymentsSerializer, CustomUserSerializer


# region CRUD user
class CreateCustomUser(CreateAPIView):
    """Создание пользователя."""

    serializer_class = CustomUserSerializer


class UpdateCustomUser(UpdateAPIView):
    """Редактирование пользователя."""

    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    serializer_class = CustomUserSerializer


class CustomUserDetail(RetrieveAPIView):
    """Просмотр данных пользователя."""

    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class DeleteCustomUser(DestroyAPIView):
    """Удаление пользователя."""

    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    serializer_class = CustomUserSerializer


# endregion


# region CRUD payment
class PaymentCreateAPIView(CreateAPIView):
    """Создание платежа."""

    permission_classes = [IsAuthenticated]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentListAPIView(ListAPIView):
    """Список платежей."""

    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["payment_day"]
    ordering = ["-payment_day"]


class PaymentUpdateAPIView(UpdateAPIView):
    """Обновление платежа."""

    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentDeleteAPIView(DestroyAPIView):
    """Удаление платежа."""

    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Payments.objects.all()
