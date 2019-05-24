from django.db import models
from django.db.models import Q, Avg, Sum
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from ubang.company.models import Company
from .import Gender

class CustomUser(AbstractUser):

    # 电话
    phone = PhoneNumberField(blank=True, null=True)

    # 姓名
    name = models.CharField(max_length=128, default='', blank=True, null=True)

    # 司机
    is_driver = models.BooleanField(default=False)
    
    # 导游
    is_tourguide = models.BooleanField(default=False)

    # 状态
    is_actived = models.BooleanField(default=True, verbose_name='Active')

    # 国家
    country = CountryField(blank=True, null=True)

    # 性别
    gender = models.IntegerField(choices=Gender.CHOICES, blank=True, null=True)

    # 微信
    wechart = models.CharField(max_length=64, blank=True, null=True)

    # wahtup
    whatsup = models.CharField(max_length=64, blank=True, null=True)

    # 头像
    avatar = models.ImageField(upload_to='photos', null=True, blank=True)

    # 介绍
    introduction = models.TextField(max_length=256, blank=True, null=True)

    # 公司
    company = models.ForeignKey(Company, related_name='user', on_delete=models.SET_NULL, blank=True,null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    @property
    def score(self):
        from ubang.booking.models import Booking
        return Booking.objects.filter(guide=self).filter(
           Q(status='Created') | Q(status='Complete')
        ).aggregate(average_score=Avg('guide_score'),total_score=Sum('guide_score'))

class Role(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(CustomUser, related_name='roles', blank=True)