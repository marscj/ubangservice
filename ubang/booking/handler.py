from django.db.models import Avg, Sum, Q
from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.conf import settings

from datetime import datetime, date, timedelta
from decimal import Decimal

from .import BookingStatus
from .models import Booking, Itinerary
from .utils import get_days
from ubang.job.models import Job
from ubang.order.models import Order
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle
from .tasks import process, complete
from ubangservice.celery import app

@receiver(pre_save, sender=Booking)
def booking_model_pre_save(sender, **kwargs):
    booking = kwargs['instance']

    if booking.bookingId is None or booking.bookingId == '':
        booking.bookingId = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')

@receiver(post_save, sender=Booking)
def booking_model_post_save(sender, **kwargs):
    booking = kwargs['instance']
    
    if kwargs['created']:
        if booking.guide:
            order = Order.objects.create(
                customer=booking.create_by.username, 
                company=booking.company_by.name, 
                start_time=booking.start_time, 
                end_time=booking.end_time,
                vehicle=booking.vehicle.traffic_plate_no,
                guide=booking.guide.username,
                discount=booking.create_by.company.discount
            )
        else:
            order = Order.objects.create(
                customer=booking.create_by.username, 
                company=booking.company_by.name, 
                start_time=booking.start_time, 
                end_time=booking.end_time,
                vehicle=booking.vehicle.traffic_plate_no,
                discount=booking.create_by.company.discount
            )

        booking.order = order
        booking.save()
        
        # process.apply_async([booking.id], eta=booking.start_time)
        complete.apply_async([booking.id], eta=booking.end_time, task_id=booking.bookingId)
        
    if booking.guide is not None:
        CustomUser.updateScore(booking.guide.id)
    
    if booking.vehicle is not None:
        Vehicle.updateScore(booking.vehicle.id)

    if booking.order and booking.status == BookingStatus.Cancel:
        booking.order.status = BookingStatus.Cancel
        booking.order.save()

    if booking.status == BookingStatus.Cancel:
        app.control.revoke(booking.bookingId)

@receiver(post_save, sender=Itinerary)
def itinerary_model_post_save(sender, **kwargs):
    itinerary = kwargs['instance']
    
    if kwargs['created']:
        days = get_days(itinerary.booking.start_time, itinerary.booking.end_time)
        first = days[0]
        last = days[-1]
        print(days)
        print(first)
        print(last)
        print(itinerary.day)
        print(itinerary.booking.start_time)
        print(itinerary.booking.end_time)
 
        if days and len(days) > 1:
            if itinerary.day == first: 
                print('I m is first')
                start_time = itinerary.booking.start_time
                end_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 23, 59, 59)
            elif itinerary.day == last:
                print('I m is last')
                start_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 0, 0, 0)
                end_time = itinerary.booking.end_time
            else:
                print('I m is mid')
                start_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 0, 0, 0)
                end_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 23, 59, 59)
        else:
            start_time = itinerary.booking.start_time
            end_time = itinerary.booking.end_time

        print(start_time)
        print(end_time)

        if itinerary.booking.guide is not None:
            Job.objects.create(
                day=itinerary.day,
                start_time=start_time,
                end_time=end_time,
                itinerary=itinerary.itinerary,
                full_day=itinerary.full_day,
                freedom_day=itinerary.freedom_day,
                guide=itinerary.booking.guide,
                vehicle=itinerary.booking.vehicle,
                booking=itinerary.booking,
            )
        else:
            Job.objects.create(
                day=itinerary.day,
                start_time=start_time,
                end_time=end_time,
                itinerary=itinerary.itinerary,
                full_day=itinerary.full_day,
                freedom_day=itinerary.freedom_day,
                vehicle=itinerary.booking.vehicle,
                booking=itinerary.booking,
            )