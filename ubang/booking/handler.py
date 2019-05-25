from django.db.models import Avg, Sum, Q
from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError

from datetime import datetime, date
from decimal import Decimal

from .models import Booking
from ubang.order.models import Order
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle

@receiver(pre_save, sender=Booking)
def booking_model_pre_save(sender, **kwargs):

    booking = kwargs['instance']
    
    if booking.bookingId is None or booking.bookingId == '':
        booking.bookingId = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')

@receiver(post_save, sender=Booking)
def booking_model_post_save(sender, **kwargs):
    booking = kwargs['instance']

    if kwargs['created']:
        order = Order.objects.create(customer=booking.create_by, company=booking.company_by)
        booking.order = order
        booking.save()
    
    if booking.guide is not None:
        CustomUser.updateScore(booking.guide.id)
    
    if booking.vehicle is not None:
        Vehicle.updateScore(booking.vehicle.id)