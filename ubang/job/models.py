from django.db import models
from django.db import Q


class TaskQuerySet(models.QuerySet):
    pass

class Task(models.Model):

    # 日期
    day = models.DateField()

    is_freedom_day = models.BooleanField(default=False, verbose_name='Freedom Day?')
    
    # 导游
    guide = models.ForeignKey(CustomUser, related_name='task', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='task', on_delete=models.SET_NULL, blank=True, null=True)

    # 内容
    itinerary = itinerary = models.CharField(max_length=128)

    # 订单
    order = models.ForeignKey(Order, related_name='task', on_delete=models.CASCADE)

    # 备注
    remark = models.CharField(max_length=256, blank=True, null=True)

    # 签到
    checkin_time = models.TimeField(default=None, blank=True, null=True)

    # 签出
    checkout_time = models.TimeField(default=None, blank=True, null=True)

    # 坐标
    checkin_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkin_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 坐标
    checkout_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    checkout_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # 图片
    checkin_picture = models.ImageField(upload_to='task/%Y/%m/%d', blank=True, null=True)

    # 图片
    checkout_picture = models.ImageField(upload_to='task/%Y/%m/%d', blank=True, null=True)

    objects = TaskQuerySet.as_manager()
    
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

        constraints = (
            models.UniqueConstraint(fields=['day', 'guide', 'is_freedom_day'], name='unique_day_guide'),
            models.UniqueConstraint(fields=['day', 'vehicle', 'is_freedom_day'], name='unique_day_vehicle'),
        )

    def __str__(self):
        return str(self.taskId)

    def validate_unique(self, exclude=None):
        if Task.objects.exclude(pk=self.pk).filter(day=self.day, is_freedom_day=self.is_freedom_day).filter(
            Q(guide=self.guide) | Q (vehicle=self.vehicle)
        ).exists():
            raise ValidationError("Task with this Day, Guide or Vehicle and Freedom Day? already exists.")
        
        return super().validate_unique(exclude)