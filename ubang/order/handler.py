from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError

from datetime import datetime, date
from decimal import Decimal

from .models import Order, Task
from .utils import save_by_task

@receiver(pre_save, sender=Order)
def order_model_pre_save(sender, **kwargs):

    order = kwargs['instance']
    
    if order.orderId is None or order.orderId == '':
        order.orderId = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')

    order.discount_name = 'no discount'
    order.discount_value = Decimal(0.0)

@receiver(post_save, sender=Order)
def task_model_post_save(sender, **kwargs):
    order = kwargs['instance']

    if kwargs['created']:
        save_by_task(order)

@receiver(pre_save, sender=Task)
def task_model_pre_save(sender, **kwargs):
    task = kwargs['instance']
    
    if task.taskId is None or task.taskId == '':
        task.taskId  = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')

    if task.is_freedom_day:
        task.itinerary = None
        task.remark = 'freedom day'