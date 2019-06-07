from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField
import arrow

from .models import Booking, Itinerary
from ubang.user.serializers import UserSerializer, UserListSerializer
from ubang.company.serializers import CompanySerializer, CompanyListSerializer
from ubang.vehicle.serializers import VehicleSerializer, VehicleListSerializer, ModelPriceSerializer
from ubang.order.serializers import OrderSerializer, OrderListSerializer

class ItinerarySerializer(serializers.ModelSerializer):

    booking = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    contact_phone = PhoneNumberField(required=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    vehicle = VehicleSerializer(required=False, allow_null=True)

    vehicle_id = serializers.IntegerField(write_only=True)

    guide = UserSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    order = OrderListSerializer(required=False, allow_null=True)

    itinerary = ItinerarySerializer(required=False, allow_null=True, many=True)

    can_save = serializers.BooleanField(required=False, read_only=True)

    can_cancel = serializers.BooleanField(required=False, read_only=True)

    can_delete = serializers.BooleanField(required=False, read_only=True)

    can_comment = serializers.BooleanField(required=False, read_only=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'contact_name', 'contact_phone', 'pick_up_addr', 'drop_off_addr',
            'create_at', 'change_at', 'status', 'create_by', 'company_by', 'vehicle', 'guide', 'vehicle_id', 'guide_id',
            'order', 'remark', 'vehicle_score', 'guide_score', 'comment', 'can_save', 'can_cancel', 
            'can_delete', 'can_comment', 'itinerary'
        )

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        contact_phone = data.get('contact_phone')
    
        if start_time and end_time:
            now = arrow.utcnow().to('Asia/Dubai')
            _start_time = arrow.get(start_time).to('Asia/Dubai')
            duration = end_time - start_time

            if start_time > end_time:
                raise serializers.ValidationError('Ensure start time is less than end time')
            
            if duration.total_seconds() < 3600:
                raise serializers.ValidationError('Ensure duration is greater than 1 hour')

            if (_start_time - now ).total_seconds() <= 3600 * 24:
                raise serializers.ValidationError('Ensure booking 1 day in advance')

        raise serializers.ValidationError('Just test1') 
        
        return data

    def create(self, validated_data):
        itinerary_data = validated_data.pop('itinerary')        
        booking = Booking.objects.create(**validated_data)
        for data in itinerary_data:
            Itinerary.objects.create(booking=booking, **data)
        return booking

    def update(self, instance, validated_data):
        itinerary_data = validated_data.pop('itinerary')
        itinerary = list(instance.itinerary.all())
        
        super().update(instance, validated_data)

        for itiner in itinerary_data:
            iti = itinerary.pop(0)
            iti.day = itiner.get('day', iti.day)
            iti.itinerary = itiner.get('itinerary', iti.itinerary)
            iti.full_day = itiner.get('full_day', iti.full_day)
            iti.freedom_day = itiner.get('freedom_day', iti.freedom_day)
            iti.vehicle_cost_charge = itiner.get('vehicle_cost_charge', iti.vehicle_cost_charge)
            iti.vehicle_gross_charge = itiner.get('vehicle_gross_charge', iti.vehicle_gross_charge)
            iti.guide_charge = itiner.get('guide_charge', iti.guide_charge)
            iti.remark = itiner.get('remark', iti.remark)
            iti.save()

        return instance

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
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'create_by', 'company_by', 'contact_name', 
            'contact_phone', 'pick_up_addr', 'drop_off_addr','remark', 'vehicle', 'vehicle_id', 'guide', 'guide_id', 
            'order', 'vehicle_score', 'guide_score', 'expiry_date'
        )

class BookingListSimpleSerializer(serializers.ModelSerializer):
    
    vehicle = VehicleListSerializer(required=False, allow_null=True)

    order = OrderListSerializer(required=False, allow_null=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'vehicle', 'order', 'create_by'
        )