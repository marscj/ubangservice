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

class BookingInline(admin.TabularInline): 
    model = Booking 
    extra = 0 
    fk_name = 'order'

    readonly_fields = (
        'bookingId',
    )

    def has_delete_permission(self, request, obj):
        return False
    
    def has_add_permission(self, request):
        return False
  

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 0
    formset = ItineraryInlineFormSet

    fields = ('day', 'itinerary', 'full_day', 'freedom_day', 'vehicle_cost_charge', 'vehicle_gross_charge', 'guide_charge', 'remark')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    inlines = (
        ItineraryInline,
    ) 

    date_hierarchy = 'start_time'

    fields = (
        'bookingId', 'confirmId', 'start_time', 'end_time', 'contact_name', 'contact_phone', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 
        'status',  'create_by', 'company_by', 'order', 'vehicle_score', 'guide_score'
    )

    readonly_fields = (
        'bookingId', #'create_by', 'company_by',
    )

    raw_id_fields = (
        'create_by', 'company_by', 'vehicle', 'guide', 'order'
    )

    list_display = (
        '__str__', 'start_time', 'end_time', 'contact_name', 'contact_phone', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 
        'status',  'create_by', 'company_by', 'order', 'itinerary'
    )
    
    def itinerary(self, obj):
        return mark_safe("<br>".join(['%s %s'% (itinerary.day,  itinerary.itinerary or '') for itinerary in obj.itinerary.all()]))

