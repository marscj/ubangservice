from rest_framework import serializers

import arrow

from .models import Job
from ubang.user.serializers import UserListSerializer
from ubang.vehicle.serializers import VehicleListSerializer

class JobSerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()

    end_time = serializers.SerializerMethodField()

    checkin_time = serializers.SerializerMethodField()

    checkout_time = serializers.SerializerMethodField()

    guide = UserListSerializer(required=False, allow_null=True, read_only=True)

    vehicle = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # vehicle = VehicleListSerializer(required=True, allow_null=True)

    booking = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Job
        fields = (
            'id', 'start_time', 'end_time', 'day', 'itinerary', 'full_day', 'freedom_day', 'remark', 'checkin_time', 'checkout_time',
            'checkin_long', 'checkin_lat', 'checkout_long', 'checkout_lat', 'checkin_picture', 'checkout_picture', 'vehicle', 'booking',
            'guide', 'status'
        )

    def get_start_time(self, obj):
        if obj.start_time is not None:
            return arrow.get(obj.start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

    def get_end_time(self, obj):
        if obj.end_time is not None:
            return arrow.get(obj.end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

    def get_checkin_time(self, obj):
        if obj.checkin_time is not None:
            return arrow.get(obj.checkin_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

    def get_checkout_time(self, obj):
        if obj.checkout_time is not None:
            return arrow.get(obj.checkout_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')