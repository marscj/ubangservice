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

    permission = PermissionSerializer(required=False, allow_null=True, many=True, read_only=True)

    company = CompanyListSerializer(required=False, allow_null=True, read_only=True)

    company_id = serializers.IntegerField(required=True, allow_null=True, write_only=True)

    permission_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, write_only=True, many=True, queryset=Permission.objects.all())

    class Meta:
        model = Role
        fields = '__all__'
    
    def create(self, validated_data):
        permissions = validated_data.pop('permission_id')
        role = Role.objects.create(**validated_data)
        
        if permissions is not None:
            for permission in permissions:
                role.permission.add(permission)
        return role

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permission_id')
        
        super().update(instance, validated_data)

        for permission in instance.permission.all():
            instance.permission.remove(permission)

        if permissions is not None:
            for permission in permissions:
                instance.permission.add(permission)

        return instance

class UserSerializer(serializers.ModelSerializer):

    country = CountryField(required=False, allow_null=True)

    phone = PhoneNumberField(required=False, allow_null=True)

    company = CompanySerializer(required=False, allow_null=True, read_only=True)

    role = RoleSerializer(required=False, allow_null=True, many=True, read_only=True)

    company_id = serializers.IntegerField(required=True, allow_null=True, write_only=True)

    role_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, write_only=True, many=True, queryset=Role.objects.all())

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'name', 'phone', 'email', 'country', 'company', 'is_driver', 'is_tourguide', 'is_actived', 'introduction', 'avg_score', 'total_score', 'is_active', 'role', 'role_id', 'company_id'
        )

    def create(self, validated_data):
        roles = validated_data.pop('role_id')
        user = CustomUser.objects.create(**validated_data)
        
        if roles is not None:
            for role in roles:
                user.role.add(role)
        return user

    def update(self, instance, validated_data):
        roles = validated_data.pop('role_id')
        
        super().update(instance, validated_data)

        for role in instance.role.all():
            instance.role.remove(role)

        if roles is not None:
            for role in roles:
                instance.role.add(role)

        return instance

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'phone')