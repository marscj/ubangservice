from django.db import models
from django.db.models import Q, Avg, Sum
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime, date

from ubang.company.models import Company
from ubang.user.models import CustomUser

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
    type = models.CharField(default=VehicleType.Car, max_length=64, choices=VehicleType.CHOICES)

    # 分类
    category = models.CharField(default=CarCategory.Mini, max_length=64, choices=VehicleCategory.CHOICES)

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

    #     Q(start_date__gte=self.start_date, start_date__lt=self.end_date)
    #    | Q(end_date__gt=self.start_date, end_date__lte=self.end_date)

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

    # 评价分
    avg_score = models.FloatField(default=0.0)

    # 总分
    total_score = models.FloatField(default=0.0)

    objects = VehicleQuerySet.as_manager()

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return self.traffic_plate_no

    @staticmethod
    def aggregate(vehicle):
        from ubang.booking.models import Booking
        aggregate = Booking.objects.filter(vehicle=vehicle).filter(
            Q(status='Created') | Q(status='Complete')
        ).aggregate(score=Avg('vehicle_score'), sum=Sum('vehicle_score'))
        return aggregate.get('score') or 0.0, aggregate.get('sum') or 0.0

    @staticmethod
    def updateScore(pk):
        from ubang.booking.models import Booking
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            avg, total = Vehicle.aggregate(vehicle)
            vehicle.avg_score = avg
            vehicle.total_score = total
            vehicle.save()
        except ObjectDoesNotExist as err:
            print(err)

class ModelPrice(models.Model):
    
    # 行程
    itinerary = models.CharField(max_length=128)

    # 全天
    full_day = models.BooleanField(default=False)

    # 价格
    cost_price = models.DecimalField(default=600.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])
    
    # 价格
    gross_price = models.DecimalField(default=800.0, max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    # 车型
    model = models.ForeignKey('Model', related_name='price', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Model Price")
        verbose_name_plural = _("Model Prices")

    def __str__(self):
        return self.itinerary