from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Booking, Itinerary
from ubang.user.serializers import UserSerializer, UserListSerializer
from ubang.company.serializers import CompanySerializer, CompanyListSerializer
from ubang.vehicle.serializers import VehicleSerializer, VehicleListSerializer, ModelPriceSerializer
from ubang.order.serializers import OrderSerializer, OrderListSerializer

class LogEntrySerializer(serializers.ModelSerializer):
    
    user = UserListSerializer(required=False, allow_null=True)
    message = serializers.SerializerMethodField()
    
    class Meta:
        model = LogEntry
        fields = ( 
            'user', 'action_time', 'message'
        )

    def get_message(self, obj):
        return obj.__str__()

class ItinerarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Itinerary
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    contact_phone = PhoneNumberField(required=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    vehicle = VehicleSerializer(required=False, allow_null=True)

    vehicle_id = serializers.IntegerField(write_only=True)

    guide = UserListSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    order = OrderListSerializer(required=False, allow_null=True)

    history = serializers.SerializerMethodField()

    itinerary = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'
    
    def get_history(self, obj):
        serializer = LogEntrySerializer(LogEntry.objects.filter(object_id=obj.id), many=True)
        return serializer.data

    def get_itinerary(self, obj):
        serializer = ItinerarySerializer(Itinerary.objects.filter(booking=obj), many=True)
        return serializer.data

class BookingListSerializer(serializers.ModelSerializer):
    
    contact_phone = PhoneNumberField(required=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    vehicle = VehicleListSerializer(required=False, allow_null=True)

    vehicle_id = serializers.IntegerField(write_only=True)

    guide = UserListSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    order = OrderListSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'create_by', 'company_by', 'contact_name', 'contact_phone', 'pick_up_addr', 'drop_off_addr', 'remark', 'vehicle', 'vehicle_id', 'guide', 'guide_id', 'order'
        )