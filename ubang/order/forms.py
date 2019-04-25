from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.forms.widgets import TextInput
from django.forms.models import ModelChoiceField

from collections import Counter

from phonenumber_field.formfields import PhoneNumberField

from .models import Order
from ubang.vehicle.models import Vehicle

class OrderForm(forms.ModelForm):

    abc = forms.ModelChoiceField
    
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
        
        if instance and instance.arrival_time:
            self.fields['arrival_time'].widget.attrs['readonly'] = True
        
        if instance and instance.departure_time:
            self.fields['departure_time'].widget.attrs['readonly'] = True

        if instance and instance.vehicle:
            self.fields['vehicle'].widget.attrs['readonly'] = True
            self.fields['vehicle'].disabled = True

        if instance and instance.guide:
            self.fields['guide'].widget.attrs['readonly'] = True
            self.fields['guide'].disabled = True

    def clean_departure_time(self):
        arrival_time = self.cleaned_data.get('arrival_time')
        departure_time = self.cleaned_data.get('departure_time')
        
        if arrival_time and departure_time:
            duration = departure_time - arrival_time

            if arrival_time > departure_time:
                raise ValidationError('Ensure arrival time is less than departure time')
            
            if duration.total_seconds() < 3600:
                raise ValidationError('Ensure duration is greater than 1 hour')
        
        return departure_time

    def get_orderId(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.orderId:
            return instance.orderId

    def clean_vehicle(self):
        vehicle = self.cleaned_data.get('vehicle')
        arrival_time = self.cleaned_data.get('arrival_time')
        departure_time = self.cleaned_data.get('departure_time')
        orderId = self.get_orderId()

        if vehicle and arrival_time and departure_time:
            if Order.objects.check_vehicle(orderId, arrival_time, departure_time, vehicle):
                raise ValidationError('Order with this time and vehicle already exists.')
         
        return vehicle

    def clean_guide(self):
        guide = self.cleaned_data.get('guide')
        arrival_time = self.cleaned_data.get('arrival_time')
        departure_time = self.cleaned_data.get('departure_time')
        orderId = self.get_orderId()

        if guide and arrival_time and departure_time:
            if Order.objects.check_guide(orderId, arrival_time, departure_time, guide):
                raise ValidationError('Order with this time and guide already exists.')
        
        return guide
    
    