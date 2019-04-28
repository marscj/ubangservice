from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

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

class OrderTimeListFilter(admin.DateFieldListFilter):
    
    def queryset(self, request, queryset):
        try:
            return queryset.exclude(**self.used_parameters)
            # return queryset.filter(**self.used_parameters)
        except (ValueError, ValidationError) as e:
            raise IncorrectLookupParameters(e)

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
            'fields': ('company', 'is_driver', 'is_tourguide', 'first_name', 'last_name', 'phone', 'email', 'wechart', 'gender', 'country', 'photo')
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
        'username', 'company', 'full_name', 'is_driver', 'is_tourguide', 'phone', 'email', 'wechart', 'gender', 'is_staff', 'is_superuser'
    )

    list_filter = (
        'company', 'gender', 'is_driver', 'is_tourguide', 'is_staff', 'is_active',
        ('order__arrival_time', admin.AllValuesFieldListFilter),
        ('order__departure_time', admin.AllValuesFieldListFilter),
        ('task__day', admin.AllValuesFieldListFilter),
    )

    search_fields = (
        'username', 'full_name', 'phone', 'email', 'wechart'
    )

    filter_horizontal = ('user_permissions',)

    raw_id_fields = ('company',)

    list_display_links = list_display