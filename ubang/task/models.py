from django.db import models
from django.db.models import Q, UniqueConstraint
from django.contrib.contenttypes.fields import GenericForeignKey 
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

from datetime import datetime, date
from decimal import Decimal

from ubang.order.models import Order
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle, ItineraryPrice
from ubang.itinerary.models import Itinerary
from .import TaskPriceType

class TaskQuerySet(models.QuerySet):
    pass

class Task(models.Model):

    taskId = models.CharField(max_length=64, default=None, null=True, editable=False)

    # 日期
    day = models.DateField()
    
    # 导游
    guide = models.ForeignKey(CustomUser, related_name='task', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='task', on_delete=models.SET_NULL, blank=True, null=True)

    # 内容
    itinerary = models.ForeignKey(Itinerary, related_name='task', on_delete=models.SET_NULL, blank=True, null=True)

    # 订单
    order = models.ForeignKey(Order, related_name='task', on_delete=models.CASCADE)

    remark = models.CharField(max_length=256, blank=True, null=True)

    objects = TaskQuerySet.as_manager()
    
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

        # unique_together = (('day', 'guide'), ('day', 'vehicle'))

        constraints = (
            models.UniqueConstraint(fields=['day', 'guide'], condition=Q(itinerary__isnull=False), name='unique_day_guide'),
            models.UniqueConstraint(fields=['day', 'vehicle'], condition=Q(itinerary__isnull=False), name='unique_day_vehicle'),
        )

    def __str__(self):
        return str(self.taskId)

    # def clean(self):
        
    #     count = Task.objects.exclude(itinerary__isnull=True).filter(
    #             Q(day=self.day) &
    #             (Q(guide=self.guide) | Q(vehicle=self.vehicle))
    #         ).count()

    #     print(count)

    #     if Task.objects.exclude(itinerary__isnull=True).filter(
    #             ~Q(taskId=self.taskId) & Q(day=self.day) &
    #             (Q(guide=self.guide) | Q(vehicle=self.vehicle))
    #         ).count() > 1:
            
    #         raise ValidationError('Task with this time and Guide or Vehicle already exists.')

    #     return super().clean()

class TaskPrice(models.Model):
    type = models.IntegerField(default=TaskPriceType.Vehicle, choices=TaskPriceType.CHOICES)
    discount_name = models.CharField(max_length=128)
    total = models.DecimalField(default=Decimal(0.0), max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    total_gross = models.DecimalField(default=Decimal(0.0), max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    extra = models.DecimalField(default=Decimal(0.0), max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    description = models.CharField(max_length=128, blank=True, null=True)
    order = models.ForeignKey(Order, related_name='price', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='price', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Task Price")
        verbose_name_plural = _("Task Prices")

    def __str__(self):
        return self.task.__str__()

class TaskProgress(models.Model):

    # 开始时间
    checkin_time = models.TimeField()

    # 结束时间
    checkout_time = models.TimeField(default=None, blank=True, null=True)

    # 坐标
    checkin_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkin_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 坐标
    checkout_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkout_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 图片
    checkin_picture = models.ImageField(upload_to='task/%Y/%m/%d', blank=True, null=True)

    # 图片
    checkout_picture = models.ImageField(upload_to='task/%Y/%m/%d', blank=True, null=True)

    order = models.ForeignKey(Order, related_name='progress', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='progress', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Task Progress")
        verbose_name_plural = _("Task Progress")

    def __str__(self):
        return str(self.id)