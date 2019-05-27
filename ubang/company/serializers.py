from rest_framework import  serializers
from django.contrib.auth.models import Permission

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Company
from ubang.discount.serializers import DiscountSerializer

class CompanySerializer(serializers.ModelSerializer):

    phone = PhoneNumberField()

    tel = PhoneNumberField()

    discount = DiscountSerializer(required=False, allow_null=True, read_only=True)
    
    class Meta:
        model = Company
        fields = '__all__'

class CompanyListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = (
           'id', 'name',
        )
