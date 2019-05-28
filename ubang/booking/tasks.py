from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

from .models import Booking
from .import BookingStatus

@shared_task
def process(pk):
    try:
        book = Booking.objects.get(pk=pk)
        book.status = BookingStatus.Process
        book.save() 
    except ObjectDoesNotExist:
        pass

@shared_task
def complete(pk):
    try:
        book = Booking.objects.get(pk=pk)
        book.status = BookingStatus.Complete
        book.save() 
    except ObjectDoesNotExist:
        pass