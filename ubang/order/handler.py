from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError

from datetime import datetime, date
from decimal import Decimal

from .models import Order
from ubang.payment.models import Payment

@receiver(pre_save, sender=Order)
def order_model_pre_save(sender, **kwargs):
    order = kwargs['instance']
    if order.orderId is None or order.orderId == '':
        order.orderId = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')
        