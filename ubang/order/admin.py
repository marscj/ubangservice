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

    confirm_template = 'admin/order/confirm.html'

    inlines = (PaymentInline, BookingInline)

    fields = (
        'orderId', 'status', 'start_time', 'end_time', ''
    )

    readonly_fields = (
        'orderId', 'customer', 'company', 'total'
    )

    list_display = (
       '__str__', 'status', 'customer', 'company', 'total', 'remark'
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

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        return False