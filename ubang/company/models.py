from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .import CompanyType
from ubang.discount.models import Discount

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
    type = models.IntegerField(default=CompanyType.Supplier, choices=CompanyType.CHOICES)

    # 价格等级
    discount = models.ForeignKey(Discount, related_name='company', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companys")

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=128, unique=True)
    index = models.IntegerField()

    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
    )

    company = models.ForeignKey(Company, related_name='role', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name