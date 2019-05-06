from rest_framework import  serializers
from django.contrib.auth.models import Permission

from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

from .models import CustomUser, Role

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    country = CountryField()

    phone = PhoneNumberField()

    roles = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'phone', 'country', 'roles', 'username', 'name', 'company', 'id'
        )

    def get_roles(self, obj):
        if obj.roles is None or obj.roles.all().count() == 0:
            return ['visitor']
        
        return obj