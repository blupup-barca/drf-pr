import django_filters
from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    sort_by_payment_date = django_filters.OrderingFilter(fields=(('payment_date', 'payment_date'),))
    paid_course = django_filters.NumberFilter(field_name='paid_course', lookup_expr='exact')
    paid_lesson = django_filters.NumberFilter(field_name='paid_lesson', lookup_expr='exact')
    method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHOD_CHOICES)

    class Meta:
        model = Payment
        fields = ['sort_by_payment_date', 'paid_course', 'paid_lesson', 'method']