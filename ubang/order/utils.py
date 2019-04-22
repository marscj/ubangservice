from django.db.models import Q
from datetime import datetime

def format_duration(duration):

    seconds = duration.total_seconds()
    hours = seconds // 3600 % 24
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    days = duration.days

    if seconds > 0.0:
        minutes = minutes + 1.0

    if minutes > 0.0:
        hours = hours + 1.0

    if hours > 0.0:
        if hours <= 4.0:
            days = days + 0.5
        else :
            days = days + 1.0

    return days
