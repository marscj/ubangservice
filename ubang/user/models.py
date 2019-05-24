from django.db import models
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

    # 平均分
    average_score = models.DecimalField(default=5.0,max_digits=10, decimal_places=2)

    # 总分
    total_score = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)

    # 公司
    company = models.ForeignKey(Company, related_name='user', on_delete=models.SET_NULL, blank=True,null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    @staticmethod
    def updateScore(pk, avg, total):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.average_score = avg
            user.total_score = total
            user.save()
        except ObjectDoesNotExist:
            pass

class Role(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(CustomUser, related_name='roles', blank=True)