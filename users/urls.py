from django.urls import path
from .views import PaymentListAPI


urlpatterns = [
    path('payments/', PaymentListAPI.as_view(), name='payment-list'),
]
