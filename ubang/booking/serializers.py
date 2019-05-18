from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Booking
from ubang.user.serializers import UserSerializer, UserListSerializer
from ubang.company.serializers import CompanySerializer, CompanyListSerializer
from ubang.vehicle.serializers import VehicleSerializer, VehicleListSerializer
from ubang.order.serializers import OrderSerializer

class BookingSerializer(serializers.ModelSerializer):

    contact_phone = PhoneNumberField(required=True)

    create_by = UserSerializer()

    company_by = CompanySerializer(required=False, allow_null=True)

    vehicle = VehicleSerializer(required=False, allow_null=True)

    guide = UserSerializer(required=False, allow_null=True)

    order = OrderSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = '__all__'


class BookingListSerializer(serializers.ModelSerializer):
    
    contact_phone = PhoneNumberField(required=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    vehicle = VehicleListSerializer(required=False, allow_null=True)

    guide = UserListSerializer(required=False, allow_null=True)

    company_by = CompanySerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'create_by', 'company_by', 'create_at', 'change_at', 'contact_name', 'contact_phone', 'vehicle', 'guide', 'status', 'parent',
        )
