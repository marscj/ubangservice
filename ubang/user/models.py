from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from ubang.company.models import Company
from .import Gender

class CustomUser(AbstractUser):

    phone = PhoneNumberField(blank=True, null=True)

    name = models.CharField(max_length=128, default='')

    is_driver = models.BooleanField(default=False)
    
    is_tourguide = models.BooleanField(default=False)

    is_actived = models.BooleanField(default=True, verbose_name='Active')

    country = CountryField(blank=True, null=True)

    gender = models.IntegerField(choices=Gender.CHOICES, blank=True, null=True)

    wechart = models.CharField(max_length=64, blank=True, null=True)

    whatsup = models.CharField(max_length=64, blank=True, null=True)

    avatar = models.ImageField(upload_to='photos', null=True, blank=True)

    company = models.ForeignKey(Company, related_name='user', on_delete=models.SET_NULL, blank=True,null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
        
class Role(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(CustomUser, related_name='roles', blank=True)