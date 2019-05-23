from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Booking, Itinerary
from ubang.user.serializers import UserSerializer, UserListSerializer
from ubang.company.serializers import CompanySerializer, CompanyListSerializer
from ubang.vehicle.serializers import VehicleSerializer, VehicleListSerializer, ModelPriceSerializer
from ubang.order.serializers import OrderSerializer, OrderListSerializer

# class LogEntrySerializer(serializers.ModelSerializer):
    
#     user = UserListSerializer(required=False, allow_null=True)
#     message = serializers.SerializerMethodField()
    
#     class Meta:
#         model = LogEntry
#         fields = ( 
#             'user', 'action_time', 'message'
#         )

#     def get_message(self, obj):
#         return obj.__str__()

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

    guide = UserListSerializer(required=False, allow_null=True)

    guide_id = serializers.IntegerField(write_only=True, required=False)

    company_by = CompanyListSerializer(required=False, allow_null=True)

    order = OrderListSerializer(required=False, allow_null=True)

    # history = serializers.SerializerMethodField()

    itinerary = ItinerarySerializer(required=False, allow_null=True, many=True)

    class Meta:
        model = Booking
        fields = '__all__'
    
    # def get_history(self, obj):
    #     serializer = LogEntrySerializer(LogEntry.objects.filter(object_id=obj.id), many=True)
    #     return serializer.data

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
            'id', 'bookingId', 'start_time', 'end_time', 'status', 'create_by', 'company_by', 'contact_name', 'contact_phone', 'pick_up_addr', 'drop_off_addr', 'remark', 'vehicle', 'vehicle_id', 'guide', 'guide_id', 'order'
        )