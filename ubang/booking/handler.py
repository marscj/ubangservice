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
from .utils import get_days, createOrder, bookingCancel
from ubang.job.models import Job
from ubang.order.models import Order
from ubang.payment.models import Payment
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
        createOrder(booking)
        complete.apply_async([booking.id], eta=booking.end_time, task_id=booking.bookingId)
        
    if booking.guide is not None:
        CustomUser.updateScore(booking.guide.id)
    
    if booking.vehicle is not None:
        Vehicle.updateScore(booking.vehicle.id)

    if booking.status == BookingStatus.Cancel:
        bookingCancel(booking)
        app.control.revoke(booking.bookingId)

@receiver(post_save, sender=Itinerary)
def itinerary_model_post_save(sender, **kwargs):
    itinerary = kwargs['instance']
    
    if kwargs['created']:
        days = get_days(itinerary.booking.start_time, itinerary.booking.end_time)
        first = days[0]
        last = days[-1]
 
        if days and len(days) > 1:
            if itinerary.day == first: 
                start_time = itinerary.booking.start_time
                end_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 23, 59, 59)
            elif itinerary.day == last:
                start_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 0, 0, 0)
                end_time = itinerary.booking.end_time
            else:
                start_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 0, 0, 0)
                end_time = datetime(itinerary.day.year, itinerary.day.month, itinerary.day.day, 23, 59, 59)
        else:
            start_time = itinerary.booking.start_time
            end_time = itinerary.booking.end_time

        if itinerary.freedom_day:
            start_time = None
            end_time = None

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
                remark=itinerary.remark
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
                remark=itinerary.remark
            )
                
        total = Decimal(0.0)
        discount = itinerary.booking.company_by.discount
        if not itinerary.freedom_day:
            total += itinerary.vehicle_charge - itinerary.vehicle_charge * discount
            total += itinerary.guide_charge
            Payment.objects.create(total=round(total, 2), remark=itinerary.itinerary, order=itinerary.booking.order)
