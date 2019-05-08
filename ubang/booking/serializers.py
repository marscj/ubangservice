from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Booking
from ubang.user.serializers import UserSerializer
from ubang.company.serializers import CompanySerializer
from ubang.vehicle.serializers import VehicleSerializer
from ubang.order.serializers import OrderSerializer

class BookingSerializer(serializers.ModelSerializer):

    contact_phone = PhoneNumberField(required=True)

    create_by = UserSerializer()

    company_by = CompanySerializer(required=False, allow_null=True)

    vehicle = VehicleSerializer()

    guide = UserSerializer(required=True, allow_null=True)

    order = OrderSerializer(required=True, allow_null=True)

    class Meta:
        model = Booking
        fields = '__all__'