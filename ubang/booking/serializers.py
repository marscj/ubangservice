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

    vehicle_id = serializers.IntegerField(write_only=True)

    guide = UserListSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'create_by', 'company_by', 'create_at', 'change_at', 'contact_name', 'contact_phone', 'pick_up_addr', 'drop_off_addr', 'remark', 'vehicle', 'vehicle_id', 'guide', 'guide_id', 'status'
        )