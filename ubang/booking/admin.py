from django.contrib import admin
from django.utils.safestring import mark_safe
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from functools import update_wrapper
from django.core.exceptions import ValidationError

from .models import Booking, Itinerary
from .forms import ItineraryInlineFormSet

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 0
    formset = ItineraryInlineFormSet

    fields = ('day', 'itinerary', 'full_day', 'freedom_day', 'vehicle_charge', 'guide_charge', 'remark')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    inlines = (
        ItineraryInline,
    ) 

    date_hierarchy = 'start_time'

    fields = (
        'bookingId', 'confirmId', 'start_time', 'end_time', 'contact_name', 'contact_phone', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 
        'status',  'create_by', 'company_by', 'vehicle_score', 'guide_score'
    )

    readonly_fields = (
        'bookingId',
    )

    raw_id_fields = (
        'create_by', 'company_by', 'vehicle', 'guide'
    )

    list_display = (
        '__str__', 'start_time', 'end_time', 'contact_name', 'contact_phone', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 
        'status',  'create_by', 'company_by', 'itinerary'
    )
    
    def itinerary(self, obj):
        return mark_safe("<br>".join(['%s %s'% (itinerary.day,  itinerary.itinerary or '') for itinerary in obj.itinerary.all()]))

