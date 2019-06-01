from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.conf import settings

from .models import Company
from .forms import CompanyForm
from ubang.user.models import CustomUser
from ubang.vehicle.models import Vehicle

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    form = CompanyForm

    fieldsets = (
        (None, {
            'fields': (
                'type', 'name', 'phone', 'tel', 'address', 'email', 'whatsup', 'wechart', 'open_time', 'close_time', 'discount',
            ),
        })
    )

    list_display = (
       '__str__', 'type', 'phone', 'tel', 'address', 'email', 'whatsup', 'wechart', 'open_time', 'close_time'
    )

    raw_id_fielsd = ('discount', )
