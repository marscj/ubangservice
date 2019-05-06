from rest_framework import  serializers
from django.contrib.auth.models import User, Permission

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    user_permissions = PermissionSerializer(required=False, many=True)

    class Meta:
        model = User
        fields = '__all__'