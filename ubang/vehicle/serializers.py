from rest_framework import serializers

from .models import Vehicle, Model, Brand


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('id',)