from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime, date

from ubang.company.models import Company
from ubang.user.models import CustomUser
from ubang.itinerary.models import Itinerary

from .import BusCategory, CarCategory, VehicleCategory, VehicleType

# 品牌
class Brand(models.Model):
    
    # 名称
    name = models.CharField(max_length=64, unique=True) 

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

def year_choices():
    return [(r,r) for r in range(2005, datetime.now().year+2)]

def current_year():
    return date(2013, 1, 1).year

# 车型
class Model(models.Model):
    
    # 名称
    name = models.CharField(max_length=64, unique=True)

    # 类型
    type = models.IntegerField(default=VehicleType.Car, choices=VehicleType.CHOICES)

    # 分类
    category = models.IntegerField(default=CarCategory.Mini, choices=VehicleCategory.CHOICES)

    # 自动挡
    is_automatic = models.BooleanField(default=True)

    # 乘客数
    passengers = models.IntegerField(default=5)

    year = models.IntegerField(choices=year_choices(), default=current_year())
    
    # 图片
    photo = models.ImageField(upload_to='model', blank=True)

    # 介绍
    introduction = models.TextField(blank=True, null=True, max_length=256)

    # 品牌
    brand = models.ForeignKey(Brand, related_name='model', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Model")
        verbose_name_plural = _("Models")

    def __str__(self):
        return self.name

class VehicleQuerySet(models.QuerySet):
    
    def filter_order(self, start_time, end_time):
        return self.exclude(
            ( Q(order__start_time__range=(start_time, end_time)) | Q(order__end_time__range=(start_time, end_time)))
        )

# 车辆 
class Vehicle(models.Model):
    
    # 车牌号
    traffic_plate_no = models.CharField(max_length=16, unique=True)     
    
    # 有效期
    exp_date = models.DateField()                    
    
    # 状态
    is_actived = models.BooleanField(default=True, verbose_name='Active')
    
    # 车型
    model = models.ForeignKey(Model, related_name='vehicle', on_delete=models.SET_NULL, null=True)

    # 供应商
    company = models.ForeignKey(Company, related_name='vehicle', on_delete=models.SET_NULL, null=True)

    # 司机
    driver = models.OneToOneField(CustomUser, related_name='car', on_delete=models.SET_NULL, blank=True, null=True)

    objects = VehicleQuerySet.as_manager()

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return self.traffic_plate_no

class ModelPrice(models.Model):
    
    cost_price = models.DecimalField(default=600.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    gross_price = models.DecimalField(default=800.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    itinerary = models.ForeignKey(Itinerary, related_name='price', on_delete=models.CASCADE)
    model = models.ForeignKey('Model', related_name='price', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Model Price")
        verbose_name_plural = _("Model Prices")

    def __str__(self):
        return str(id)