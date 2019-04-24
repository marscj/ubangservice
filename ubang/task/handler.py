from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string

from datetime import datetime, date

from .models import Task
 
@receiver(pre_save, sender=Task)
def task_model_pre_save(sender, **kwargs):
    task = kwargs['instance']
    
    if task.taskId is None:
        task.taskId  = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')
    
# @receiver(post_save, sender=Task)
# def task_model_post_save(sender, **kwargs):
#     if kwargs['created'] is True:
#         print('Created: {}'.format(kwargs['instance'].__dict__))
#     else:
#         print('Updated: {}'.format(kwargs['instance'].__dict__))