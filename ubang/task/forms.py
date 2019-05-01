from django import forms
from django.core.exceptions import ValidationError

from datetime import datetime, date

from .models import Task
from ubang.vehicle.models import ItineraryPrice

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
            if vehicle.model and vehicle.model.it_price:
                try:
                    vehicle.model.it_price.all().get(itinerary=itinerary)
                except ItineraryPrice.DoesNotExist:
                    raise ValidationError('Ensure %s model has itinerary price' % vehicle.traffic_plate_no)
            else:
                raise ValidationError('Ensure %s has model' % vehicle.traffic_plate_no)

    def clean_guide(self, guide):
        if guide and not guide.is_tourguide:
            raise ValidationError('Ensure %s is tourguide user' % guide)

        if guide and not guide.is_actived:
            raise ValidationError('Ensure %s is active' % guide)

    def clean_vehicle(self, vehicle):
        if vehicle and not vehicle.is_actived:
            raise ValidationError('Ensure %s is active' % vehicle.traffic_plate_no)

    def clean(self):
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                order = form.cleaned_data.get('order')
                vehicle = form.cleaned_data.get('vehicle')
                guide = form.cleaned_data.get('guide')
                itinerary = form.cleaned_data.get('itinerary')
                day = form.cleaned_data.get('day')

                self.clean_order_time(order, day)
                self.clean_itinerary(itinerary, vehicle)
                self.clean_guide(guide)
                self.clean_vehicle(vehicle)
                
        return super().clean()