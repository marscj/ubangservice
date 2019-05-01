from django.contrib import admin

from .models import ItineraryPrice, Brand, Model, Vehicle
from .forms import ModelForm, VehicleForm
from ubang.vehicle import VehicleType, VehicleCategory

class ItineraryPriceInlie(admin.TabularInline):
    model = ItineraryPrice
    extra = 0

    raw_id_fields = ('itinerary',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = (ItineraryPriceInlie, )

    form = ModelForm

    fields = ('brand', 'type', 'category', 'name', 'passengers', 'year', 'is_automatic',  'photo', 'introduction')

    list_display = fields

    list_display_links = list_display

    raw_id_fields = ('brand',)

class OrderTimeListFilter(admin.DateFieldListFilter):
    
    def queryset(self, request, queryset):
        try:
            return queryset.exclude(**self.used_parameters)
            # return queryset.filter(**self.used_parameters)
        except (ValueError, ValidationError) as e:
            raise IncorrectLookupParameters(e)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    form = VehicleForm
    
    fields = ('traffic_plate_no', 'model', 'company', 'driver', 'exp_date', 'is_actived')

    list_display = ('traffic_plate_no', 'brand', 'model', 'type', 'category', 'passengers', 'company', 'driver', 'exp_date', 'is_actived')

    list_display_links = ('traffic_plate_no', 'brand', 'model', 'type', 'category', 'passengers', 'company', 'driver', 'exp_date')

    raw_id_fields = ('model', 'company', 'driver')

    list_editable = ('is_actived', )

    readonly_fields = ('brand', 'type', 'category', 'passengers')

    list_filter = (
        'is_actived', 'model__brand', 'model__type', 'model__category', 
        ('order__start_time', OrderTimeListFilter),
        ('order__end_time', OrderTimeListFilter),
        'task__day',
        'task__is_freedom_day'
    )

    def brand(self, obj):
        if obj.model:
            return obj.model.brand
    
    def type(self, obj):
        if obj.model:
            return obj.model.type
    
    def category(self, obj):
        if obj.model:
            return obj.model.category

    def passengers(self, obj):
        if obj.model:
            return obj.model.passengers

    def type(self, obj):
        if obj.model:
            return VehicleType.CHOICES[obj.model.type][1]

    def category(self, obj):
        if obj.model:
            return VehicleCategory.CHOICES[obj.model.category][1]