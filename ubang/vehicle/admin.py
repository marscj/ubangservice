from django.contrib import admin

from .models import Brand, Model, Vehicle, ModelPrice
from .forms import ModelForm, VehicleForm
from ubang.vehicle import VehicleType, VehicleCategory

class ModelPriceInlie(admin.TabularInline):
    model = ModelPrice
    extra = 0

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = (ModelPriceInlie, )

    form = ModelForm

    fields = ('brand', 'type', 'category', 'name', 'passengers', 'year', 'is_automatic',  'photo', 'introduction')

    list_display = fields

    list_display_links = list_display

    raw_id_fields = ('brand',)

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
        'is_actived', 'model__brand', 'model__type', 'model__category'
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