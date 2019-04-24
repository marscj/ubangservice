from django.conf import settings
from decimal import Decimal

from .models import Task, TaskPrice, TaskProgress
from .import TaskPriceType

def total(cost_price, gross_price, discount):
    return gross_price - abs(gross_price - cost_price) * discount

def get_vehicle_price(itinerary, vehicle, discount=Decimal(0.0)):
    if itinerary and vehicle and vehicle.model:
        try: 
            price = vehicle.model.it_price.all().get(itinerary=itinerary)
            return price.gross_price, total(price.cost_price, price.gross_price, discount)
        except ItineraryPrice.DoesNotExist:
            print('Ensure This vehicle model has itinerary price')
    
    return None, None

def get_guide_price(itinerary, guide):
    if itinerary and guide:
        if itinerary.is_fullday:
            return settings.DEFAULT_GUIDE_PRICE, settings.DEFAULT_GUIDE_PRICE
        else:
            return settings.DEFAULT_GUIDE_PRICE / Decimal(2.0), settings.DEFAULT_GUIDE_PRICE / Decimal(2.0)

    return None, None

def get_or_create_taskprice(order, task, type=TaskPriceType.Vehicle, discount_name='no discount', total=Decimal(0.0), total_gross=Decimal(0.0), extra=Decimal(0.0), description=None):
    return TaskPrice.objects.get_or_create(order=order, task=task, type=type, discount_name=discount_name, total=total, total_gross=total_gross, extra=extra, description=description)

def delete_price(task, type):
    try:
        return TaskPrice.objects.get(task=task, type=type).delete()
    except TaskPrice.DoesNotExist:
        pass