from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

import pytz
from datetime import datetime, timedelta

from phonenumber_field.modelfields import PhoneNumberField

from .import BookingStatus
from ubang.vehicle.models import Vehicle, ModelPrice
from ubang.user.models import CustomUser
from ubang.order.models import Order
from ubang.company.models import Company

class BookingQuerySet(models.QuerySet):
    pass

class Booking(models.Model):
    
    # 预定号
    bookingId = models.CharField(max_length=64, editable=False)

    # 确认号
    confirmId = models.CharField(max_length=128, blank=True, null=True, default='')

    # 开始时间
    start_time = models.DateTimeField()

    # 结束时间
    end_time = models.DateTimeField()

    # 联系人姓名
    contact_name = models.CharField(max_length=64)

    # 联系人电话
    contact_phone = PhoneNumberField()

    # 送车地址
    pick_up_addr = models.CharField(max_length=128, blank=True, null=True, verbose_name='Pick up address')

    # 还车地址
    drop_off_addr = models.CharField(max_length=128, blank=True, null=True, verbose_name='Drop off address')

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 修改时间
    change_at = models.DateTimeField(auto_now=True)

    # 状态
    status = models.CharField(max_length=16, default=BookingStatus.Created, choices=BookingStatus.CHOICES)
        
    # 客户
    create_by = models.ForeignKey(CustomUser, related_name='booking_customer', on_delete=models.SET_NULL, null=True, verbose_name = 'Customer', editable=False) 

    # 公司
    company_by = models.ForeignKey(Company, related_name='booking', on_delete=models.SET_NULL, null=True, verbose_name = 'Company', editable=False)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='booking', on_delete=models.SET_NULL, blank=True, null=True)

    # 导游
    guide = models.ForeignKey(CustomUser, related_name='booking_guide', on_delete=models.SET_NULL, blank=True, null=True)

    # 订单
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, blank=True, null=True)

    # 备注
    remark = models.TextField(max_length=256, blank=True, null=True)

    # 车辆得分
    vehicle_score = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    # 导游得分
    guide_score = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    # 评论
    comment = models.TextField(max_length=256, blank=True, null=True)

    objects = BookingQuerySet.as_manager()

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.bookingId
        
    @property
    def expiry_date(self):
        return self.start_time - timedelta(days=1)

    @property
    def can_save(self):  
        if self.status == BookingStatus.Created or self.status == BookingStatus.Complete:
            return True
        return False

    @property
    def can_cancel(self):
        if self.status == BookingStatus.Created:
            return True
        return False

    @property
    def can_delete(self):
        # if self.status == BookingStatus.Cancel:
        #     return True
        return False

    @property
    def can_comment(self):
        if self.status == BookingStatus.Complete:
            return True
        return False

class Itinerary(models.Model):
    
    # 日期
    day = models.DateField()

    # 行程
    itinerary = models.CharField(max_length=128)

    # 全天
    full_day = models.BooleanField(default=False)

    # 自由日
    freedom_day = models.BooleanField(default=False)

    # 车辆价格
    vehicle_cost_charge = models.DecimalField(default=600.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    
    # 车辆价格
    vehicle_gross_charge = models.DecimalField(default=800.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    # 导游价格
    guide_charge = models.DecimalField(default=0.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    # 备注
    remark = models.CharField(max_length=256, blank=True, null=True)

    # 订单
    booking = models.ForeignKey(Booking, related_name='itinerary', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Itinerary")
        verbose_name_plural = _("Itinerarys")

    def __str__(self):
        return self.itinerary
