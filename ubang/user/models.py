from django.db import models
from django.db.models import Q, Avg, Sum
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from ubang.company.models import Company
from .import Gender

class Permission(models.Model):
    label = models.CharField(max_length=128, unique=True)
    key = models.IntegerField()

    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return self.label

class Role(models.Model):
    name = models.CharField(max_length=128)
    
    permission = models.ManyToManyField(Permission, blank=True)

    company = models.ForeignKey(Company, related_name='role', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name

class CustomUserQuerySet(UserManager):
    def filter_job(self, start_time, end_time):
        return self.exclude(
            Q(booking_guide__status='Created') &
            (Q(job__start_time__range=(start_time, end_time), job__freedom_day=False) | 
            Q(job__end_time__range=(start_time, end_time), job__freedom_day=False))
        )
    
    def valide_job(self, id, start_time, end_time):
        return self.filter(pk=id).filter(
            Q(booking_guide__status='Created') &
            (Q(job__start_time__range=(start_time, end_time), job__freedom_day=False) | 
            Q(job__end_time__range=(start_time, end_time), job__freedom_day=False))
        ).exists()

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
    avg_score = models.FloatField(default=0.0)

    # 总分
    total_score = models.FloatField(default=0.0)

    # 角色
    role = models.ManyToManyField(Role, blank=True)

    # 公司
    company = models.ForeignKey(Company, related_name='user', on_delete=models.SET_NULL, blank=True,null=True)

    objects = CustomUserQuerySet()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    @staticmethod
    def aggregate(user):
        from ubang.booking.models import Booking
        aggregate = Booking.objects.filter(guide=user).filter(status='Complete').aggregate(score=Avg('guide_score'), sum=Sum('guide_score'))
        return aggregate.get('score') or 0.0, aggregate.get('sum') or 0.0

    @staticmethod
    def updateScore(pk):
        from ubang.booking.models import Booking
        try:
            user = CustomUser.objects.get(pk=pk)
            avg, total = CustomUser.aggregate(user)
            user.avg_score = avg
            user.total_score = total
            user.save()
        except ObjectDoesNotExist as err:
            print(err)

    # @property
    # def avg_score(self):
    #     from ubang.booking.models import Booking
    #     return round(Booking.objects.filter(guide=self).filter(
    #        Q(status='Created') | Q(status='Complete')
    #     ).aggregate(score=Avg('guide_score')).get('score') or 0.0, 2) 
    
    # @property
    # def total_score(self):
    #     from ubang.booking.models import Booking
    #     return round(Booking.objects.filter(guide=self).filter(
    #        Q(status='Created') | Q(status='Complete')
    #     ).aggregate(score=Sum('guide_score')).get('score') or 0.0, 2)