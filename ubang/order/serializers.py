from rest_framework import serializers

from .models import Order
from ubang.user.serializers import UserSerializer
from ubang.vehicle.serializers import VehicleSerializer
from ubang.company.serializers import CompanySerializer

class OrderSerializer(serializers.ModelSerializer):

    guide = UserSerializer(required=True)

    vehicle = VehicleSerializer()

    customer = UserSerializer()

    company = CompanySerializer(required=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id', 'orderId'
        )