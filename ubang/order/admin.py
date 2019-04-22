from django.contrib import admin
from django.utils.html import format_html
from django.core.exceptions import ValidationError

from datetime import datetime

from .models import Order
from .forms import OrderForm
from ubang.task.admin import TaskInline, TaskPriceInline, TaskProgressInline
from ubang.payment.admin import PaymentInline

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    form = OrderForm

    inlines = (TaskInline, TaskPriceInline, TaskProgressInline, PaymentInline, )

    fieldsets = ( 
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('orderId', 'status', 'contact_name', 'contact_phone', 'start_time', 'end_time', 'pick_up_addr', 'drop_off_addr', 'discount_name', 'total', 'remark', 'link', 'hyper_link')}
        ),
        ('Customer Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('customer', 'customer_name', 'customer_phone', 'customer_company', 'customer_company_phone', 'customer_company_tel', 'customer_company_address', 'customer_company_discount')}
        ),

        ('Create Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('create_at', 'change_at')}
        )
    )

    list_display = (
       'orderId', 'status', 'customer', 'contact_name', 'contact_phone', 'start_time', 'end_time', 'pick_up_addr', 'drop_off_addr', 'discount_name', 'total', 'remark', 'hyper_link'
    )

    list_display_links = list_display

    raw_id_fields = (
        'customer',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'orderId', 'contact_name', 'contact_phone', 'start_time', 'end_time'
    )

    readonly_fields = (
        'orderId', 'create_at', 'change_at', 'discount_name', 'total', 'hyper_link', 'customer', 'customer_name', 'customer_phone', 'customer_company', 'customer_company_phone', 'customer_company_tel', 'customer_company_address', 'customer_company_discount'
    )

    def hyper_link(self, obj):
        return format_html("<a href='{0}'>{0}</a>", obj.link)

    hyper_link.short_description = 'Hyperlink'

    
    def save_model(self, request, obj, form, change):
        
        if obj.customer is None:
            obj.customer = request.user

        super().save_model(request, obj, form, change)