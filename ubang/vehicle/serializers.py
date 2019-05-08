from rest_framework import serializers

from .models import Vehicle, Model, Brand, ModelPrice
from ubang.company.serializers import CompanySerializer
from ubang.user.serializers import UserSerializer

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):

    brand = BrandSerializer()

    class Meta:
        model = Model
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):

    model = ModelSerializer()

    company = CompanySerializer()

    driver = UserSerializer()

    class Meta:
        model = Vehicle
        fields = ('id',)