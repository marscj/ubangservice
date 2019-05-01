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
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    model = Image
    extra = 1

class DateTimeListFilter(admin.DateFieldListFilter):

    def queryset(self, request, queryset):
        print(self.used_parameters)
        try:
            return queryset.exclude(**self.used_parameters)
            # return queryset.filter(**self.used_parameters)
        except (ValueError, ValidationError) as e:
            raise IncorrectLookupParameters(e)

class TaskDayListFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.field_generic = '%s__' % field_path
        self.date_params = {k: v for k, v in params.items() if k.startswith(self.field_generic)}

        now = timezone.now()
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()
            
        tomorrow = today + datetime.timedelta(days=1)
        if today.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=today.month + 1, day=1)
        next_year = today.replace(year=today.year + 1, month=1, day=1)

        self.lookup_kwarg = '%s' % field_path
        
        self.links = (
            (_('Any date'), {}),
            (_('Today'), {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(tomorrow),
            }),
            (_('Past 7 days'), {
                self.lookup_kwarg_since: str(today - datetime.timedelta(days=7)),
                self.lookup_kwarg_until: str(tomorrow),
            }),
            (_('This month'), {
                self.lookup_kwarg_since: str(today.replace(day=1)),
                self.lookup_kwarg_until: str(next_month),
            }),
            (_('This year'), {
                self.lookup_kwarg_since: str(today.replace(month=1, day=1)),
                self.lookup_kwarg_until: str(next_year),
            }),
        )
        if field.null:
            self.lookup_kwarg_isnull = '%s__isnull' % field_path
            self.links += (
                (_('No date'), {self.field_generic + 'isnull': 'True'}),
                (_('Has date'), {self.field_generic + 'isnull': 'False'}),
            )
        super().__init__(field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        params = [self.lookup_kwarg,]
        if self.field.null:
            params.append(self.lookup_kwarg_isnull)
        return params

    def choices(self, changelist):
        for title, param_dict in self.links:
            yield {
                'selected': self.date_params == param_dict,
                'query_string': changelist.get_query_string(param_dict, [self.field_generic]),
                'display': title,
            }

@admin.register(CustomUser)
class CustomerUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm

    inlines = (ImageInline, )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'company', 'is_driver', 'is_tourguide', 'first_name', 'last_name', 'phone', 'email', 'wechart', 'gender', 'country', 'photo'),
        }),
    )

    fieldsets = (
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('username', 'password')}
        ),
        (_('Personal info'), {
            'classes': ('grp-collapse grp-open',),
            'fields': ('company', 'is_actived', 'is_driver', 'is_tourguide', 'first_name', 'last_name', 'phone', 'email', 'wechart', 'gender', 'country', 'photo')
        }),
        (_('Permissions'), {
            'classes': ('grp-collapse grp-open',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Important dates'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('last_login', 'date_joined')
        }),
    )

    list_display = (
        'username', 'company', 'full_name', 'is_driver', 'is_tourguide', 'phone', 'email', 'wechart', 'gender', 'is_staff', 'is_superuser', 'is_actived'
    )

    list_display_links = (
        'username', 'company', 'full_name', 'phone', 'email', 'wechart', 'gender', 'is_staff', 'is_superuser',
    )

    list_filter = (
        'company', 'gender', 'is_driver', 'is_tourguide', 'is_staff', 'is_actived',
        ('order__start_time', DateTimeListFilter),
        ('order__end_time', DateTimeListFilter),
        'task__day',
        'task__is_freedom_day'
    )

    search_fields = (
        'username', 'phone', 'email', 'wechart', 'order__start_time'
    )

    list_editable = (
        'is_actived', 'is_driver', 'is_tourguide'
    )

    filter_horizontal = ('user_permissions',)

    raw_id_fields = ('company',)