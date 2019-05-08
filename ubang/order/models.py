from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal

from datetime import datetime, date

from ubang.user.models import CustomUser
from ubang.company.models import Company
from ubang.vehicle.models import Vehicle
from ubang.itinerary.models import Itinerary
from .import OrderStatus

class OrderQueryset(models.QuerySet):
    
    def check_vehicle(self, orderId, start_time, end_time, vehicle):
        return self.filter(
            Q(vehicle=vehicle) & ~Q(orderId=orderId) &
            (Q(start_time__range=(start_time, end_time)) | Q(end_time__range=(start_time, end_time)))
        ).exists()

    def check_guide(self, orderId, start_time, end_time, guide):
        return self.filter(
            Q(guide=guide) & ~Q(orderId=orderId) &
            (Q(start_time__range=(start_time, end_time)) | Q(end_time__range=(start_time, end_time)))
        ).exists()

class Order(models.Model):
    
    # id
    orderId = models.CharField(max_length=64, unique=True, editable=False)

    # 开始时间
    start_time = models.DateTimeField()

    # 结束时间
    end_time = models.DateTimeField()

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 修改时间
    change_at = models.DateTimeField(auto_now_add=True)
    
    # 订单状态
    status = models.IntegerField(default=OrderStatus.Open, choices=OrderStatus.CHOICES)

    # 导游
    guide = models.ForeignKey(CustomUser, related_name='order_guide', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='order', on_delete=models.SET_NULL, null=True)

    # 客户
    customer = models.ForeignKey(CustomUser, related_name='order_customer', on_delete=models.SET_NULL, null=True, editable=False)
    
    # 公司
    company = models.ForeignKey(Company, related_name='order', on_delete=models.SET_NULL, null=True, editable=False)

    applyId = models.CharField(max_length=64, editable=False, blank=True, null=True)

    # 备注
    remark = models.TextField(max_length=256, blank=True, null=True)

    objects = OrderQueryset.as_manager()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.orderId)

    def can_confirm(self):
        return self.status == OrderStatus.Draft

    def can_cancel(self):
        return self.status == OrderStatus.Confirm

    def confirm(self):
        if self.can_confirm():
            self.status = OrderStatus.Confirm
            self.save()

    def cancel(self):
        if self.can_cancel():
            self.status = OrderStatus.Cancel
            self.save()

    @property
    def total(self):
        total = Decimal(0.0)
        return total

class TaskQuerySet(models.QuerySet):
    pass

class Task(models.Model):

    taskId = models.CharField(max_length=64, default=None, null=True, editable=False)

    # 日期
    day = models.DateField()

    is_freedom_day = models.BooleanField(default=False, verbose_name='Freedom Day?')
    
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

        constraints = (
            models.UniqueConstraint(fields=['day', 'guide', 'is_freedom_day'], name='unique_day_guide'),
            models.UniqueConstraint(fields=['day', 'vehicle', 'is_freedom_day'], name='unique_day_vehicle'),
        )

    def __str__(self):
        return str(self.taskId)

    def validate_unique(self, exclude=None):
        if Task.objects.exclude(pk=self.pk).filter(day=self.day, is_freedom_day=self.is_freedom_day).filter(
            Q(guide=self.guide) | Q (vehicle=self.vehicle)
        ).exists():
            raise ValidationError("Task with this Day, Guide or Vehicle and Freedom Day? already exists.")
        
        return super().validate_unique(exclude)

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