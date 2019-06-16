from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from datetime import datetime

from .models import Order
from .forms import OrderForm
from .import OrderStatus
from ubang.payment.admin import PaymentInline
from ubang.booking.admin import BookingInline

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    form = OrderForm

    inlines = (PaymentInline,)

    fields = (
        'orderId', 'status', 'start_time', 'end_time', 'vehicle', 'guide', 'customer', 'company', 'discount', 'total', 'remark'
    )

    readonly_fields = (
        'orderId', 'status', 'start_time', 'end_time', 'vehicle', 'guide', 'customer', 'company', 'discount', 'total'
    )

    list_display = (
       '__str__', 'status', 'start_time', 'end_time', 'vehicle', 'guide', 'customer', 'company', 'discount', 'total', 'total'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'orderId', 
    )

    # class Media:
    #     js = [
    #         'admin/js/order.js',
    #         'admin/js/task.js'
    #     ]