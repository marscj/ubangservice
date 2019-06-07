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
from .models import Booking
from ubang.order.models import Order
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle
from .tasks import process, complete

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
        complete.apply_async([booking.id], eta=booking.end_time)
        
    if booking.guide is not None:
        CustomUser.updateScore(booking.guide.id)
    
    if booking.vehicle is not None:
        Vehicle.updateScore(booking.vehicle.id)