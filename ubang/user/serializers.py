from rest_framework import  serializers

from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

from .models import CustomUser, Role, Permission
from ubang.company.serializers import CompanySerializer, CompanyListSerializer

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    permission = PermissionSerializer(required=False, allow_null=True, many=True)

    company = CompanyListSerializer(required=False, allow_null=True)

    class Meta:
        model = Role
        fields = (
          'name'
        )

class UserSerializer(serializers.ModelSerializer):

    country = CountryField(required=False, allow_null=True)

    phone = PhoneNumberField(required=False, allow_null=True)

    company = CompanySerializer(required=False, allow_null=True)

    role = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'name', 'phone', 'email', 'country', 'company', 'is_driver', 'is_tourguide', 'is_actived', 'introduction', 'avg_score', 'total_score', 'is_active', 'role'
        )

    def get_role(self, obj):
        return ['admin']

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'name')