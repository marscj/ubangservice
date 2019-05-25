from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.admin.options import IncorrectLookupParameters

import datetime
from django.utils import timezone

from .models import CustomUser
from .forms import CustomUserCreationForm
from ubang.resource.models import Image

admin.site.site_title = 'UBang'
admin.site.site_header = 'UBang Service'
admin.site.index_title = 'UBang Service Administration'

class ImageInline(GenericTabularInline):
    model = Image
    extra = 1

@admin.register(CustomUser)
class CustomerUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm

    inlines = (ImageInline, )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'company', 'is_driver', 'is_tourguide', 'name', 'phone', 'wechart', 'email', 'gender', 'country', 'avatar'),
        }),
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')}
        ),
        (_('Personal info'), {
            'fields': ('company', 'is_actived', 'is_driver', 'is_tourguide', 'name', 'phone', 'wechart', 'email', 'gender', 'country', 'avatar', 'avg_score', 'total_score', 'introduction')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    list_display = (
        '__str__', 'company', 'name', 'is_driver', 'is_tourguide', 'phone', 'wechart', 'email', 'gender', 'is_staff', 'is_superuser', 'is_actived'
    )

    list_filter = (
        'company', 'gender', 'is_driver', 'is_tourguide', 'is_staff', 'is_actived',
    )

    readonly_fields = (
        'avg_score', 'total_score'
    )

    search_fields = (
        'phone', 'email', 'wechart'
    )

    list_editable = (
        'is_actived', 'is_driver', 'is_tourguide'
    )

    filter_horizontal = (
        'user_permissions',
    )

    raw_id_fields = (
        'company',
    )