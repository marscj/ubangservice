from django.db.models import Q
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from datetime import date, datetime, timedelta

from ubang.task.models import Task

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

def save_by_customer(order):
    if order and order.create_by:
        order.customer_name = order.create_by.full_name
        order.customer_phone = order.create_by.phone

        if order.create_by.company:
            order.customer_company = order.create_by.company.name
            order.customer_company_phone = order.create_by.company.phone
            order.customer_company_tel = order.create_by.company.tel
            order.customer_company_address = order.create_by.company.address

            if order.create_by.company.discount:
                order.customer_company_discount = order.create_by.company.discount.name

                if order.discount_name is None or order.discount_value is None:
                    order.discount_name = order.create_by.company.discount.name
                    order.discount_value = order.create_by.company.discount.value
        order.save()

def save_by_task(order):
    days = get_days(order.arrival_time, order.departure_time)

    print('#####333')
    for day in days:
        print(day)
        create_task(order=order, day=day, guide=order.guide, vehicle=order.vehicle)
    print('#####444')
        

 