from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.forms.widgets import TextInput
from django.forms.models import ModelChoiceField

from datetime import datetime, date

from phonenumber_field.formfields import PhoneNumberField

from .models import Order, Task
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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     instance = getattr(self, 'instance', None)
        
    #     if instance and instance.start_time:
    #         self.fields['start_time'].widget.attrs['readonly'] = True
    #         self.fields['start_time'].disabled = True
        
    #     if instance and instance.end_time:
    #         self.fields['end_time'].widget.attrs['readonly'] = True
    #         self.fields['end_time'].disabled = True

    #     if instance and instance.vehicle:
    #         self.fields['vehicle'].widget.attrs['readonly'] = True
    #         self.fields['vehicle'].disabled = True

    #     if instance and instance.guide:
    #         self.fields['guide'].widget.attrs['readonly'] = True
    #         self.fields['guide'].disabled = True

    # def clean_end_time(self):
    #     start_time = self.cleaned_data.get('start_time')
    #     end_time = self.cleaned_data.get('end_time')
        
    #     if start_time and end_time:
    #         duration = end_time - start_time

    #         if start_time > end_time:
    #             raise ValidationError('Ensure arrival time is less than departure time')
            
    #         if duration.total_seconds() < 3600:
    #             raise ValidationError('Ensure duration is greater than 1 hour')
        
    #     return end_time

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

class TaskInlineFormSet(forms.BaseInlineFormSet):
    
    def clean_order_time(self, order, day):
        arrival_day = date(order.start_time.year, order.start_time.month, order.start_time.day)
        departure_day = date(order.end_time.year, order.end_time.month, order.end_time.day)

        if order and day: 
            if day < arrival_day:
                raise ValidationError('Ensure day is greater than or equal to %s' % arrival_day)

            if day > departure_day:
                raise ValidationError('Ensure day is less than or equal to %s' % departure_day)

    def clean_itinerary(self, itinerary, vehicle):
        if itinerary and vehicle:
            if vehicle.model and vehicle.model.price:
                try:
                    vehicle.model.price.all().get(itinerary=itinerary)
                except ModelPrice.DoesNotExist:
                    raise ValidationError('Ensure %s model has itinerary price' % vehicle.traffic_plate_no)
            else:
                raise ValidationError('Ensure %s has model' % vehicle.traffic_plate_no)

    # def clean_guide(self, guide):
    #     if guide and not guide.is_tourguide:
    #         raise ValidationError('Ensure %s is tourguide user' % guide)

    #     if guide and not guide.is_actived:
    #         raise ValidationError('Ensure %s is active' % guide)

    # def clean_vehicle(self, vehicle):
    #     if vehicle and not vehicle.is_actived:
    #         raise ValidationError('Ensure %s is active' % vehicle.traffic_plate_no)

    # def clean(self):
    #     for form in self.forms:
    #         if form.cleaned_data and not form.cleaned_data.get('DELETE'):
    #             order = form.cleaned_data.get('order')
    #             vehicle = form.cleaned_data.get('vehicle')
    #             guide = form.cleaned_data.get('guide')
    #             itinerary = form.cleaned_data.get('itinerary')
    #             day = form.cleaned_data.get('day')

    #             self.clean_order_time(order, day)
    #             self.clean_itinerary(itinerary, vehicle)
    #             self.clean_guide(guide)
    #             self.clean_vehicle(vehicle)
                
    #     return super().clean()