from django.db import models
from django.db.models import Q
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
from ubang.vehicle.models import Vehicle
from ubang.itinerary.models import Itinerary
from .import TaskPriceType

class TaskQuerySet(models.QuerySet):
    
    def check_vehicle(self, start_time, end_time, vehicle, taskId):
        try :
            qs = self.filter(
                Q(vehicle=vehicle) & ~Q(taskId=taskId) &
                (Q(start_datetime__range=(start_time, end_time)) | Q(end_datetime__range=(start_time, end_time)))
            )
        except Task.vehicle.RelatedObjectDoesNotExist:
            raise ValidationError('Vehicle does not exist')

        return qs.count() > 0

    def check_guide(self, start_time, end_time, guide, taskId):
        try :
            qs = self.filter(
                Q(guide=guide) & ~Q(taskId=taskId) &
                (Q(start_datetime__range=(start_time, end_time)) | Q(end_datetime__range=(start_time, end_time)))
            )
        except Task.vehicle.RelatedObjectDoesNotExist:
            raise ValidationError('Guide does not exist')

        return qs.count() > 0

class Task(models.Model):

    taskId = models.CharField(max_length=64, default=None, null=True, editable=False)

    # 日期
    day = models.DateField()

    # 开始时间
    start_time = models.TimeField()

    # 结束时间
    end_time = models.TimeField()

    # 开始时间
    start_datetime = models.DateTimeField(blank=True, null=True)

    # 结束时间
    end_datetime = models.DateTimeField(blank=True, null=True)

    # 是否是全天
    is_fullday = models.BooleanField(default=False, blank=True, null=True)
    
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

    def __str__(self):
        return str(self.taskId)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.taskId is None:
                self.taskId  = datetime.now().strftime('%Y%m%d') + '-%d-%d' % (self.id, self.order.customer.id)

        self.start_datetime = datetime.combine(self.day, self.start_time)
        self.end_datetime = datetime.combine(self.day, self.end_time)
        self.is_fullday = (datetime.combine(self.day, self.end_time) - datetime.combine(self.day, self.start_time)).total_seconds() >= 3600 * 6

        super().save(*args, **kwargs)

        self.configure_price()

    def get_or_create_price(self, type):
        return TaskPrice.objects.get_or_create(order=self.order, task=self, type=type)

    def delete_price(self, type):
        try:
            return TaskPrice.objects.get(task=self, type=type).delete()
        except TaskPrice.DoesNotExist:
            pass

    def get_itinerary_price(self):
        try:
            return self.vehicle.model.it_price.all().get(itinerary = self.itinerary)
        except ItineraryPrice.DoesNotExist:
            raise ValidationError('Ensure This vehicle model has itinerary price')
            
    def total(self, discount, price):
        return price.gross_price - abs(price.gross_price - price.cost_price) * discount

    def configure_price(self):
        if self.vehicle:
            vehicle_price = self.get_or_create_price(TaskPriceType.Vehicle)[0]
            itinerary_price = self.get_itinerary_price()

            if self.order.discount_name:
                vehicle_price.discount_name = self.order.discount_name
            
            vehicle_price.total_gross = itinerary_price.gross_price
            vehicle_price.total = self.total(self.order.discount_value, itinerary_price)
                
            vehicle_price.save()
        else:
            self.delete_price(TaskPriceType.Vehicle)
            
        if self.guide:
            guide_price = self.get_or_create_price(TaskPriceType.Guide)[0]
            guide_price.discount = 0.0
            if self.is_fullday:
                guide_price.total_gross = settings.DEFAULT_GUIDE_PRICE
                guide_price.total = settings.DEFAULT_GUIDE_PRICE
            else:
                guide_price.total_gross = settings.DEFAULT_GUIDE_PRICE / Decimal(2.0)
                guide_price.total = settings.DEFAULT_GUIDE_PRICE / Decimal(2.0)
            guide_price.save()
        else:
            self.delete_price(TaskPriceType.Guide)

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