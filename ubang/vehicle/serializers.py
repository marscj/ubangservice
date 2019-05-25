from rest_framework import serializers

from .models import Vehicle, Model, Brand, ModelPrice
from ubang.company.serializers import CompanySerializer
from ubang.user.serializers import UserSerializer

class ModelPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelPrice
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):

    brand = BrandSerializer()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Model
        fields = '__all__'

    def get_price(self, obj):
        serializer = ModelPriceSerializer(ModelPrice.objects.filter(model=obj), many=True)
        return serializer.data        

class VehicleDetailSerializer(serializers.ModelSerializer):

    model = ModelSerializer()

    company = CompanySerializer()

    driver = UserSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    
    model = ModelSerializer()

    avg_score = serializers.FloatField(required=False, allow_null=True, read_only=True)

    total_score = serializers.FloatField(required=False, allow_null=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'id', 'traffic_plate_no'
        )