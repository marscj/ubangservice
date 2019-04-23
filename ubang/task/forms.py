from django import forms
from django.core.exceptions import ValidationError

from datetime import datetime, date

from .models import Task
from ubang.vehicle.models import ItineraryPrice

class TaskInlineFormSet(forms.BaseInlineFormSet):
    
    def clean_time(self, start_time, end_time):
        if start_time and end_time:
            duration = datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)

            if start_time > end_time:
                raise ValidationError('Ensure start time is less than end time')
            
            if duration.total_seconds() < 3600:
                raise ValidationError('Ensure duration is greater than 1 hour')

    def clean_order_time(self, order, start_time, end_time):
        if order and start_time and end_time:
            if start_time < order.start_time:
                raise ValidationError('Ensure start time is greater than or equal to %s' % order.start_time)

            if end_time > order.end_time:
                raise ValidationError('Ensure end time is less than or equal to %s' % order.end_time)

    def clean_itinerary(self, itinerary, vehicle):
        if itinerary and vehicle and vehicle.model and vehicle.model.it_price:
            try:
                vehicle.model.it_price.all().get(itinerary=itinerary)
            except ItineraryPrice.DoesNotExist:
                raise ValidationError('Ensure %s model has itinerary price' % vehicle.traffic_plate_no)
        else:
            raise ValidationError('Ensure %s model has itinerary price' % vehicle.traffic_plate_no)

    def clean_is_guide(self, guide):
        if guide and not guide.is_tourguide:
            raise ValidationError('Ensure %s is tourguide user' % guide)

    def clean_vehicle(self, start_time, end_time, vehicle, taskId):
        if start_time and end_time and vehicle:

            if not vehicle.is_active:
                raise ValidationError('Ensure %s is active' % vehicle.traffic_plate_no)

            if Task.objects.check_vehicle(start_time, end_time, vehicle, taskId):
                raise ValidationError('Ensure %s has no other task' % vehicle.traffic_plate_no)

    def clean_guide(self, start_time, end_time, guide, taskId):
        if start_time and end_time and guide:
            if Task.objects.check_guide(start_time, end_time, guide, taskId):
                raise ValidationError('Ensure %s has no other task' % guide.__str__())
    
    def clean_fullday(self, fullday, itinerary):
        if fullday is not None and itinerary is not None and itinerary:
            if fullday != itinerary.is_fullday:
                raise ValidationError('Ensure kindly enter correct timings')

    def clean(self):
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                taskId = form.cleaned_data.get('id')
                order = form.cleaned_data.get('order')
                vehicle = form.cleaned_data.get('vehicle')
                guide = form.cleaned_data.get('guide')
                itinerary = form.cleaned_data.get('itinerary')
                day = form.cleaned_data.get('day')
                start_time = form.cleaned_data.get('start_time')
                end_time = form.cleaned_data.get('end_time')

                if day and start_time and end_time:
                    start_datetime = datetime.combine(day, start_time)
                    end_datetime = datetime.combine(day, end_time)
                    self.clean_order_time(order, start_datetime, end_datetime)
                    self.clean_vehicle(start_datetime, end_datetime, vehicle, taskId)
                    self.clean_guide(start_datetime, end_datetime, guide, taskId)

                    print((end_datetime - start_datetime).total_seconds(), 3600 * 6, start_datetime, end_datetime)
                    self.clean_fullday((end_datetime - start_datetime).total_seconds() >= 3600 * 6, itinerary)

                self.clean_time(start_time, end_time)
                self.clean_itinerary(itinerary, vehicle)
                self.clean_is_guide(guide)
                
        return super().clean()