from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField
import arrow

from .models import Booking, Itinerary
from ubang.user.serializers import UserSerializer, UserListSerializer
from ubang.company.serializers import CompanySerializer, CompanyListSerializer
from ubang.vehicle.serializers import VehicleSerializer, VehicleListSerializer, ModelPriceSerializer
from ubang.vehicle.models import Vehicle
from ubang.user.models import CustomUser

class ItinerarySerializer(serializers.ModelSerializer):

    booking = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    contact_phone = PhoneNumberField(required=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    create_by_id = serializers.IntegerField(write_only=True, required=False)

    vehicle = VehicleSerializer(required=False, allow_null=True)

    vehicle_id = serializers.IntegerField(write_only=True)

    guide = UserSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    company_by_id = serializers.IntegerField(write_only=True, required=False)

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
            'remark', 'vehicle_score', 'guide_score', 'comment', 'can_save', 'can_cancel', 
            'can_delete', 'can_comment', 'itinerary', 'confirmId', 'company_by_id', 'create_by_id'
        )

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        vehicle_id = data.get('vehicle_id')
        guide_id = data.get('guide_id')
        create_by_id = data.get('create_by_id')
        company_by_id = data.get('company_by_id')
    
        if start_time is not None and end_time is not None:
            now = arrow.utcnow().to('Asia/Dubai')
            _start_time = arrow.get(start_time).to('Asia/Dubai')
            _start = arrow.get(start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            _end = arrow.get(end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            duration = end_time - start_time

            if start_time > end_time:
                raise serializers.ValidationError('Ensure start time is less than end time')
            
            if duration.total_seconds() < 3600:
                raise serializers.ValidationError('Ensure duration is greater than 1 hour')

            # if (_start_time - now ).total_seconds() <= 3600 * 24:
            #     raise serializers.ValidationError('Ensure booking 1 day in advance')

            if vehicle_id is not None:
                if Vehicle.objects.valide_job(vehicle_id, _start, _end):
                    raise serializers.ValidationError('Ensure vehicle is free.')

            if guide_id is not None:
                if CustomUser.objects.valide_job(guide_id, _start, _end):
                    raise serializers.ValidationError('Ensure vehicle is free.')

            if vehicle_id is None:
                raise serializers.ValidationError('Vehicle is required.')

            if create_by_id is None:
                raise serializers.ValidationError('creator is none.')

            if company_by_id is None:
                raise serializers.ValidationError('you are not a company user.')

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
            iti.vehicle_charge = itiner.get('vehicle_charge', iti.vehicle_charge)
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

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'create_by', 'company_by', 'contact_name', 
            'contact_phone', 'pick_up_addr', 'drop_off_addr','remark', 'vehicle', 'vehicle_id', 'guide', 'guide_id', 
            'vehicle_score', 'guide_score', 'expiry_date', 'confirmId'
        )

class BookingListSimpleSerializer(serializers.ModelSerializer):
    
    vehicle = VehicleListSerializer(required=False, allow_null=True)

    create_by = UserListSerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'vehicle', 'create_by', 'confirmId'
        )

class BookingObjSerializer(serializers.ModelSerializer):
    contact_phone = PhoneNumberField(required=True)

    company_by = serializers.StringRelatedField(required=False, allow_null=True, read_only=True)

    class Meta:
        model = Booking
        fields = (
            'id', 'bookingId', 'contact_name', 'contact_phone', 'pick_up_addr', 'drop_off_addr', 'company_by'
        )
    