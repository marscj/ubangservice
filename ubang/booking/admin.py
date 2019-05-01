from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from mptt.admin import MPTTModelAdmin
from mptt.forms import TreeNodeChoiceField 

from .models import Booking, Itinerary
from .forms import ItineraryInlineFormSet

class BookingInlineForm(forms.BaseInlineFormSet): 
    tree_field = TreeNodeChoiceField(queryset=Booking.objects.all()) 

class BookingInline(admin.TabularInline): 
    model = Booking 
    formset = BookingInlineForm 
    extra = 0 
    fk_name = 'order'

    exclude = (
        'pick_up_addr', 'drop_off_addr', 'remark', 
    )

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

    fields = ('day', 'is_freedom_day', 'itinerary', 'remark')

    # readonly_fields = ('day', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ('taskId', 'guide', 'vehicle', 'day')

    # def has_delete_permission(self, request, obj):
    #     return False

    # def has_add_permission(self, request):
    #     return False

@admin.register(Booking)
class BookingAdmin(MPTTModelAdmin):

    inlines = (
        ItineraryInline,
    )

    list_display = (
        'bookingId', 'apply', 'start_time', 'end_time', 'vehicle', 'guide', 'contact_name', 'contact_phone',  'create_at', 'itinerary'
    )
    
    def itinerary(self, obj):
        return mark_safe("<br>".join(['%s %s'% (itinerary.day,  itinerary.itinerary or '') for itinerary in obj.itinerary.all()]))

