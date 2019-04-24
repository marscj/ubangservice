from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal
from datetime import datetime

from ubang.user.models import CustomUser
from ubang.company.models import Discount
from ubang.vehicle.models import Vehicle

from .import OrderStatus
from .validators import customer_validator

class OrderQueryset(models.QuerySet):
    pass

class Order(models.Model):
    
    # id
    orderId = models.CharField(max_length=64, default=None, null=True, editable=False)

    # 开始时间
    arrival_time = models.DateTimeField()

    # 结束时间
    departure_time = models.DateTimeField()
    
    # 订单状态
    status = models.IntegerField(default=OrderStatus.Open, choices=OrderStatus.CHOICES)

    # 送车地址
    pick_up_addr = models.CharField(max_length=128, blank=True, null=True)

    # 还车地址
    drop_off_addr = models.CharField(max_length=128, blank=True, null=True)

    # 联系人姓名
    contact_name = models.CharField(max_length=64)

    # 联系人电话
    contact_phone = PhoneNumberField()

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 最后修改时间
    change_at = models.DateTimeField(auto_now=True)
        
    # 备注
    remark = models.TextField(max_length=256, blank=True, null=True)

    # link
    link = models.URLField(default='', blank=True)

    # 客户
    customer = models.ForeignKey(CustomUser, related_name='order_customer', on_delete=models.SET_NULL, null=True)

    # 客户名称
    customer_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='name')

    # 客户电话
    customer_phone = PhoneNumberField(blank=True, null=True, verbose_name='phone')

    # 客户公司
    customer_company = models.CharField(max_length=128, blank=True, null=True, verbose_name='company')

    # 客户公司电话
    customer_company_phone = models.CharField(max_length=128, blank=True, null=True, verbose_name='company phone')

    # 客户公司固定电话
    customer_company_tel = models.CharField(max_length=128, blank=True, null=True, verbose_name='company tel')

    # 客户公司地址
    customer_company_address = models.CharField(max_length=128, blank=True, null=True, verbose_name='company address')

    # 客户公司折扣
    customer_company_discount = models.CharField(max_length=128, blank=True, null=True, verbose_name='company discount')

    # 折扣
    discount_name = models.CharField(max_length=128, default=None, null=True)

    discount_value = models.DecimalField(default=None, max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True, editable=False)

    # 导游
    guide = models.ForeignKey(CustomUser, related_name='order', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='order', on_delete=models.SET_NULL, blank=True, null=True)

    objects = OrderQueryset.as_manager()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.orderId)

    @property
    def total(self):
        total = Decimal(0.0)
        for price in self.price.all():
            total += price.total
        
        return total

    def save(self, *args, **kwargs):
        if self.orderId is None:
            self.orderId = datetime.now().strftime('%Y%m%d%H%M%S') + '-%s' % get_random_string(4, allowed_chars='0123456789')

        self.discount_name = 'no discount'
        self.discount_value = Decimal(0.0)

        if self.customer:
            self.customer_name = self.customer.full_name
            self.customer_phone = self.customer.phone

            if self.customer.company:
                self.customer_company = self.customer.company.name
                self.customer_company_phone = self.customer.company.phone
                self.customer_company_tel = self.customer.company.tel
                self.customer_company_address = self.customer.company.address

                if self.customer.company.discount:
                    self.customer_company_discount = self.customer.company.discount.name

                    if self.discount_name is None or self.discount_value is None:
                        self.discount_name = self.customer.company.discount.name
                        self.discount_value = self.customer.company.discount.value

        super().save(*args, **kwargs)