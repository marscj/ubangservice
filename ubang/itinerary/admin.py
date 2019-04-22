from django.contrib import admin

from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'is_fullday')

    list_display_links = list_display
