from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import Booking
from ubang.user.serializers import UserSerializer
from ubang.company.serializers import CompanySerializer

class BookingSerializer(serializers.ModelSerializer):

    phone = PhoneNumberField(required=true)

    create_by = UserSerializer()

    company_by = CompanySerializer(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = '__all__'