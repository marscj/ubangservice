from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel

from ubang.vehicle.models import Vehicle
from ubang.user.models import CustomUser
from ubang.order.models import Order
from ubang.company.models import Company
from ubang.itinerary.models import Itinerary as _Itinerary

class BookingQuerySet(models.QuerySet):
    pass

class Booking(MPTTModel):
    
    bookingId = models.CharField(max_length=64, editable=False)

    # 联系人姓名
    contact_name = models.CharField(max_length=64)

    # 联系人电话
    contact_phone = PhoneNumberField()

    # 开始时间
    start_time = models.DateTimeField()

    # 结束时间
    end_time = models.DateTimeField()

    # 送车地址
    pick_up_addr = models.CharField(max_length=128, blank=True, null=True, verbose_name='Pick up address')

    # 还车地址
    drop_off_addr = models.CharField(max_length=128, blank=True, null=True, verbose_name='Drop off address')

    # 有效期
    expiry_date = models.DateTimeField(default=now)
        
    # 备注
    remark = models.TextField(max_length=256, blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True, editable=False)

    # 客户
    create_by = models.ForeignKey(CustomUser, related_name='booking_customer', on_delete=models.SET_NULL, null=True, verbose_name = 'Customer', editable=False) 

    # 公司
    company_by = models.ForeignKey(Company, related_name='booking', on_delete=models.SET_NULL, null=True, verbose_name = 'Company', editable=False)
    
    # 车辆
    vehicle = models.ForeignKey(Vehicle, related_name='booking', on_delete=models.SET_NULL, blank=True, null=True)

    # 导游
    guide = models.ForeignKey(CustomUser, related_name='booking_guide', on_delete=models.SET_NULL, blank=True, null=True)

    # 订单
    order = models.ForeignKey(Order, related_name='booking', on_delete=models.CASCADE, blank=True, null=True)

    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    objects = BookingQuerySet.as_manager()

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.bookingId

    @property
    def apply(self):
        if self.order:
            return self.order.applyId == self.bookingId
        return False

class Itinerary(models.Model):
    
    # 日期
    day = models.DateField()

    # 内容
    itinerary = models.ForeignKey(_Itinerary, related_name='itinerary', on_delete=models.SET_NULL, blank=True, null=True)

    # 订单
    booking = models.ForeignKey(Booking, related_name='itinerary', on_delete=models.CASCADE)

    remark = models.CharField(max_length=256, blank=True, null=True)
    
    class Meta:
        verbose_name = _("Itinerary")
        verbose_name_plural = _("Itinerarys")

    def __str__(self):
        return str(self.id)
