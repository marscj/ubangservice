from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Brand, Model, Vehicle, ModelPrice
from .forms import ModelForm, VehicleForm
from ubang.vehicle import VehicleType, VehicleCategory

class ModelPriceInlie(admin.TabularInline):
    model = ModelPrice
    extra = 0

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display =  (
        '__str__',
    )

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = (ModelPriceInlie, )

    form = ModelForm

    fields = (
        'brand', 'type', 'category', 'name', 'passengers', 'year', 'is_automatic',  'photo', 'introduction'
    )

    list_display =  (
        '__str__', 'brand', 'type', 'category', 'passengers', 'year', 'is_automatic',  'photo', 'introduction', 'model_price'
    )

    raw_id_fields = []

    def model_price(self, obj):
        return mark_safe("<br>".join(['%s,cost(%s),gross(%s)'% (price.itinerary, price.cost_price, price.gross_price) for price in obj.price.all()]))

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    form = VehicleForm
    
    fields = (
        'traffic_plate_no', 'model', 'company', 'driver', 'exp_date', 'is_actived', 'avg_score', 'total_score'
    )

    list_display = (
        '__str__', 'brand', 'model', 'type', 'category', 'passengers', 'company', 'driver', 'exp_date', 'is_actived'
    )

    raw_id_fields = (
        'driver', 'model',
    )

    list_editable = (
        'is_actived',
    )

    readonly_fields = (
        'avg_score', 'total_score'
    )

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
            
    def model_price(self, obj):
        if obj.model:
            return mark_safe("<br>".join(['%s,cost(%s),gross(%s)'% (price.itinerary, price.cost_price, price.gross_price) for price in obj.model.price.all()]))