from rest_framework import  serializers
from django.contrib.auth.models import Permission

from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

from .models import CustomUser, Role
from ubang.company.serializers import CompanySerializer, CompanyListSerializer

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    country = CountryField(required=False, allow_null=True)

    phone = PhoneNumberField(required=False, allow_null=True)

    roles = serializers.SerializerMethodField()

    company = CompanyListSerializer(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'name', 'phone', 'email', 'country', 'company', 'roles', 'is_driver', 'is_tourguide', 'is_actived', 'introduction', 'avg_score', 'total_score'
        )

    def get_roles(self, obj):
        if obj.roles is None or obj.roles.all().count() == 0:
            return ['visitor']
        
        return obj

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'name')