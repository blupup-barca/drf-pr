from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateApiView, PaymentsListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment"),
]