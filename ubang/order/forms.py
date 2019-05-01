from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.forms.widgets import TextInput
from django.forms.models import ModelChoiceField

from collections import Counter

from phonenumber_field.formfields import PhoneNumberField

from .models import Order
from ubang.booking.models import Booking
from ubang.vehicle.models import Vehicle

class OrderForm(forms.ModelForm):
    
    contact_phone = PhoneNumberField(
        required=True,
        initial='+971',
        help_text='+971 XXX XXXXXXX'
    )

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        instance = getattr(self, 'instance', None)
        
        if instance and instance.start_time:
            self.fields['start_time'].widget.attrs['readonly'] = True
            self.fields['start_time'].disabled = True
        
        if instance and instance.end_time:
            self.fields['end_time'].widget.attrs['readonly'] = True
            self.fields['end_time'].disabled = True

        if instance and instance.vehicle:
            self.fields['vehicle'].widget.attrs['readonly'] = True
            self.fields['vehicle'].disabled = True

        if instance and instance.guide:
            self.fields['guide'].widget.attrs['readonly'] = True
            self.fields['guide'].disabled = True

    def clean_end_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        
        if start_time and end_time:
            duration = end_time - start_time

            if start_time > end_time:
                raise ValidationError('Ensure arrival time is less than departure time')
            
            if duration.total_seconds() < 3600:
                raise ValidationError('Ensure duration is greater than 1 hour')
        
        return end_time

    def get_orderId(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.orderId:
            return instance.orderId

    def clean_vehicle(self):
        vehicle = self.cleaned_data.get('vehicle')
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        orderId = self.get_orderId()

        if vehicle and start_time and end_time:
            if Order.objects.check_vehicle(orderId, start_time, end_time, vehicle):
                raise ValidationError('Order with this time and vehicle already exists.')
         
        if vehicle and not vehicle.is_actived:
            raise ValidationError('Ensure %s is active' % vehicle.traffic_plate_no)

        return vehicle

    def clean_guide(self):
        guide = self.cleaned_data.get('guide')
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        orderId = self.get_orderId()

        if guide and start_time and end_time:
            if Order.objects.check_guide(orderId, start_time, end_time, guide):
                raise ValidationError('Order with this time and guide already exists.')

        if guide and not guide.is_tourguide:
            raise ValidationError('Ensure %s is tourguide user' % guide)

        if guide and not guide.is_actived:
            raise ValidationError('Ensure %s is active' % guide)
        
        return guide
    