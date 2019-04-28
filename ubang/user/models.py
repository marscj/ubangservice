from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings

from datetime import date
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from ubang.company.models import Company
from .import Gender

class CustomUser(AbstractUser):

    phone = PhoneNumberField(blank=True, null=True)

    is_driver = models.BooleanField(default=False)
    
    is_tourguide = models.BooleanField(default=False)

    is_actived = models.BooleanField(default=True, verbose_name='Active')

    country = CountryField(blank=True, null=True)

    gender = models.IntegerField(choices=Gender.CHOICES, blank=True, null=True)

    wechart = models.CharField(max_length=64, blank=True, null=True)

    whatsup = models.CharField(max_length=64, blank=True, null=True)

    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    company = models.ForeignKey(Company, related_name='user', on_delete=models.SET_NULL,blank=True,null=True)

    # order = models.ManyToManyField(Order, related_name='user', through='OrderUser')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
        
    @property
    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

# class OrderUserQueryset(models.QuerySet):
#     pass

# class OrderUser(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='order_user', on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, related_name='order_user', on_delete=models.CASCADE)

#     objects = OrderUserQueryset.as_manager

#     class Meta:
#         verbose_name = _("OrderUser")
#         verbose_name_plural = _("OrderUsers")

#     def __str__(self):
#         return self.user.__str__()

#     @property
#     def is_driver(self):
#         return self.user.is_driver

#     @property
#     def is_tourguide(self):
#         return self.user.is_tourguide

#     @property
#     def full_name(self):
#         return self.user.full_name
    
#     @property
#     def phone(self):
#         return self.user.phone

#     @property
#     def per_day_price(self):
#         return self.user.per_day_price.amount

#     @property
#     def total(self):
#         if self.per_day_price and self.order.days:
#             return self.per_day_price * Decimal(self.order.days)

#     def check_user_order(self):
#         try :
#             qs = OrderUser.objects.filter(
#                 Q(user=self.user) & ~Q(order=self.order) &
#                 ( Q(order__start_time__range=(self.order.start_time, self.order.end_time)) | Q(order__start_time__range=(self.order.start_time, self.order.end_time)))
#             )
#         except OrderUser.user.RelatedObjectDoesNotExist:
#             raise ValidationError('User does not exist')

#         print(qs)
#         return qs.count() == 0

#     def clean(self):

#         if not self.is_driver and not self.is_tourguide:
#             raise ValidationError('%s is not a driver or tourguide' % (self.user.username))

#         if not self.check_user_order():
#             raise ValidationError('%s has other orders at this time' % (self.user.username))