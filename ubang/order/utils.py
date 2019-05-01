from django.db.models import Q
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.conf import settings

from datetime import date, datetime, timedelta
from decimal import Decimal

from .models import Task, TaskProgress

def format_duration(duration):
    
    seconds = duration.total_seconds()
    hours = seconds // 3600 % 24
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    days = duration.days

    if seconds > 0:
        minutes = minutes + 1

    if minutes > 0:
        hours = hours + 1

    if hours > 0:
        days = days + 1

    return days

def get_days(start, end):
    duration = date(end.year, end.month, end.day) + timedelta(days=1) - date(start.year, start.month, start.day)
    return [(date(start.year, start.month, start.day) + timedelta(days=index)).strftime('%Y-%m-%d') for index in range(duration.days) ]

def create_task(order, day, guide, vehicle, itinerary=None):
    return Task.objects.get_or_create(order=order, day=day, guide=guide, vehicle=vehicle)

def save_by_task(order):
    days = get_days(order.start_time, order.end_time)

    return [create_task(order=order, day=day, guide=order.guide, vehicle=order.vehicle) for day in days]

def total(cost_price, gross_price, discount):
    return gross_price - abs(gross_price - cost_price) * discount

 