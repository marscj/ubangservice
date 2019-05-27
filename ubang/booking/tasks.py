from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

from .models import Booking

@shared_task
def change_status(pk, status):
    try:
        book = Booking.objects.get(pk=pk)
        book.status = status
        book.save()
    except ObjectDoesNotExist:
        pass