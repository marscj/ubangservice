from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal


from ubang.user.models import CustomUser
from ubang.company.models import Discount
from ubang.vehicle.models import Vehicle

from .import OrderStatus
from .validators import customer_validator

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
    
    # 订单状态
    status = models.IntegerField(default=OrderStatus.Draft, choices=OrderStatus.CHOICES)

    # 客户
    customer = models.ForeignKey(CustomUser, related_name='order', on_delete=models.SET_NULL, null=True, verbose_name = 'Customer')
    
    # 公司
    company = models.ForeignKey(Company, related_name='booking', on_delete=models.SET_NULL, null=True, verbose_name = 'Company', editable=False)
    
    # 导游
    guide = models.ForeignKey(CustomUser, related_name='order', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='order', on_delete=models.SET_NULL, null=True)

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

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
        for price in self.price.all():
            total += price.total
        
        return total