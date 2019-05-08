from rest_framework import  serializers
from django.contrib.auth.models import Permission

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    phone = PhoneNumberField()

    tel = PhoneNumberField()
    
    class Meta:
        model = Company
        fields = ('id', 'name',)

