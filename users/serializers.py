from rest_framework import serializers
from users.models import User, Payments
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PaymentsSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not data.get("course") and not data.get("lessons"):
            raise serializers.ValidationError("Нужно выбрать курс или урок для оплаты.")
        return data

    class Meta:
        model = Payments
        fields = "__all__"
