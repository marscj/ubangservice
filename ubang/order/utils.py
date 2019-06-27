from django.db.models import Q
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.conf import settings

from datetime import date, datetime, timedelta
from decimal import Decimal

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

 