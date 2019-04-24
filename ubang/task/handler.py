from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils.crypto import get_random_string

from datetime import datetime, date

from .models import Task, TaskPrice, TaskProgress
from .utils import (
    get_or_create_taskprice, get_guide_price, get_vehicle_price, delete_price
)
 
@receiver(pre_save, sender=Task)
def task_model_pre_save(sender, **kwargs):
    task = kwargs['instance']
    
    if task.taskId is None:
        task.taskId  = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')
    
@receiver(post_save, sender=Task)
def task_model_post_save(sender, **kwargs):
    task = kwargs['instance']

    guide_total_gross, guide_total = get_guide_price(task.itinerary, task.guide)
    if guide_total_gross and guide_total:
        get_or_create_taskprice(order=task.order, task=task, total=guide_total, total_gross=guide_total_gross)

    vehicle_total_gross, vehicle_total = get_vehicle_price(task.itinerary, task.vehicle, task.order.discount_value)
    if vehicle_total_gross and vehicle_total:
        get_or_create_taskprice(order=task.order, task=task, total=vehicle_total, total_gross=vehicle_total_gross, discount_name=task.order.discount_name)

    if task.guide is None:
        delete_price(task=task)

    

@receiver(pre_delete, sender=Task)
def task_model_pre_delete(sender, **kwargs):
    print(kwargs)