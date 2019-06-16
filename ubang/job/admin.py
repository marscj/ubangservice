from django.contrib import admin

from .models import Job
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    
    fields = (
        'day', 'start_time', 'end_time', 'itinerary', 'full_day', 'freedom_day', 'guide', 'vehicle', 'booking', 
        'checkin_time', 'checkout_time'
    )

    list_display = fields

    raw_id_fields = (
        'guide', 'vehicle', 'booking'
    )
