from django import forms
from django.core.exceptions import ValidationError

from datetime import datetime, date

from .models import Booking
from ubang.vehicle.models import ItineraryPrice

class ItineraryInlineFormSet(forms.BaseInlineFormSet):
    
    def clean_booking_time(self, booking, day):
        arrival_day = date(booking.arrival_time.year, booking.arrival_time.month, booking.arrival_time.day)
        departure_day = date(booking.departure_time.year, booking.departure_time.month, booking.departure_time.day)

        if booking and day: 
            if day < arrival_day:
                raise ValidationError('Ensure day is greater than or equal to %s' % arrival_day)

            if day > departure_day:
                raise ValidationError('Ensure day is less than or equal to %s' % departure_day)

    def clean(self):
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                booking = form.cleaned_data.get('booking')
                itinerary = form.cleaned_data.get('itinerary')
                day = form.cleaned_data.get('day')

                self.clean_booking_time(booking, day)
                
        return super().clean()