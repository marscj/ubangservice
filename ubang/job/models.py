from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from ubang.booking.models import Booking
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle

class JobQuerySet(models.QuerySet):
    pass

class Job(models.Model):

    # 日期
    day = models.DateField()

    # 开始时间
    start_time = models.DateTimeField()

    # 结束时间
    end_time = models.DateTimeField()

    # 行程
    itinerary = models.CharField(max_length=128)

    # 全天
    full_day = models.BooleanField(default=False)

    # 自由日
    freedom_day = models.BooleanField(default=False)
    
    # 导游
    guide = models.ForeignKey(CustomUser, related_name='job', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='job', on_delete=models.SET_NULL, blank=True, null=True)

    # 订单
    booking = models.ForeignKey(Booking, related_name='job', on_delete=models.CASCADE)

    # 备注
    remark = models.CharField(max_length=256, blank=True, null=True)

    # 签到
    checkin_time = models.DateTimeField(default=None, blank=True, null=True)

    # 签出
    checkout_time = models.DateTimeField(default=None, blank=True, null=True)

    # 坐标
    checkin_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkin_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 坐标
    checkout_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkout_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 图片
    checkin_picture = models.ImageField(upload_to='job/%Y/%m/%d', blank=True, null=True)

    # 图片
    checkout_picture = models.ImageField(upload_to='job/%Y/%m/%d', blank=True, null=True)

    objects = JobQuerySet.as_manager()
    
    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        
    def __str__(self):
        return str(self.itinerary)

    # def validate_unique(self, exclude=None):
    #     if Task.objects.exclude(pk=self.pk).filter(day=self.day, is_freedom_day=self.is_freedom_day).filter(
    #         Q(guide=self.guide) | Q (vehicle=self.vehicle)
    #     ).exists():
    #         raise ValidationError("Task with this Day, Guide or Vehicle and Freedom Day? already exists.")
        
    #     return super().validate_unique(exclude)