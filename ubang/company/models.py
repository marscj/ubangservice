from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from phonenumber_field.modelfields import PhoneNumberField

from decimal import Decimal

from .import CompanyType

# 组织
class Company(models.Model):
    
    # 名称    
    name = models.CharField(max_length=128, unique=True)

    # 移动电话
    phone = PhoneNumberField()

    # 固定电话
    tel = PhoneNumberField()
    
    # 地址
    address = models.CharField(max_length=256)

    # email
    email = models.EmailField()
    
    # 微信
    wechart = models.CharField(max_length=64, default='', blank=True)
    
    # whatsup
    whatsup = models.CharField(max_length=64, default='')

    # 营业时间
    open_time = models.TimeField(default='09:00', auto_now=False, auto_now_add=False)
    
    # 营业时间
    close_time = models.TimeField(default='18:00', auto_now=False, auto_now_add=False)

    # 组织类型
    type = models.CharField(default=CompanyType.Supplier, max_length=16, choices=CompanyType.CHOICES)

    # 折扣
    discount = models.DecimalField(default=Decimal(0.0), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companys")

    def __str__(self):
        return self.name