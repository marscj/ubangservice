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
from ubang.discount.models import Discount
from .import OrderStatus

class OrderQueryset(models.QuerySet):
    pass

class Order(models.Model):
    # id
    orderId = models.CharField(max_length=64, unique=True, editable=False)

    # 订单状态
    status = models.CharField(max_length=16, default=OrderStatus.Created, choices=OrderStatus.CHOICES)

    # 开始时间
    start_time = models.DateTimeField()

    # 结束时间
    end_time = models.DateTimeField()

    # 车牌号
    vehicle = models.CharField(max_length=128)
    
    # 导游账号
    guide = models.CharField(max_length=128, blank=True, null=True)

    # 客户账号
    customer = models.CharField(max_length=128)
    
    # 公司名称
    company = models.CharField(max_length=128)

    # 折扣
    discount = models.DecimalField(default=Decimal(0.0), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    # 备注
    remark = models.TextField(max_length=256, blank=True, null=True)

    objects = OrderQueryset.as_manager()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.orderId)

    def can_cancel(self):
        return self.status == OrderStatus.Created

    def cancel(self):
        if self.can_cancel():
            self.status = OrderStatus.Cancel
            self.save()

    @property
    def total(self):
        total = Decimal(0.0)
        return total