from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

from decimal import Decimal

from phonenumber_field.modelfields import PhoneNumberField

from .import CompanyType

class Discount(models.Model):
    
    name = models.CharField(max_length=128)
    value = models.DecimalField(default=Decimal(0.0), max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    class Meta:
        verbose_name = _("Disscount")
        verbose_name_plural = _("Disscounts")

    def __str__(self):
        return self.name

# 组织
class Company(Group):
    
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
    type = models.IntegerField(default=CompanyType.Supplier, choices=CompanyType.CHOICES)

    # 价格等级
    discount = models.ForeignKey(Discount, related_name='company', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companys")

    def __str__(self):
        return self.name
    
