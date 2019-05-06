from rest_framework import  serializers
from django.contrib.auth.models import Permission

from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

from .models import CustomUser

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    country = CountryField()

    phone = PhoneNumberField()

    user_permissions = PermissionSerializer(required=False, many=True)
    # PermissionSerializer(required=False, many=True)

    class Meta:
        model = CustomUser
        fields = '__all__'