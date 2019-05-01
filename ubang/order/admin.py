from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from datetime import datetime

from .models import Order
from .forms import OrderForm, TaskInlineFormSet
from .import OrderStatus
from ubang.payment.admin import PaymentInline
from ubang.booking.admin import BookingInline
from .models import Task, TaskProgress

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    formset = TaskInlineFormSet

    class Media:
        js = [
            'admin/js/task.js'
        ]
    
    fields = ('taskId', 'day', 'is_freedom_day', 'itinerary', 'guide', 'vehicle', 'remark')

    raw_id_fields = ('vehicle', 'guide', )

    readonly_fields = ('taskId', 'day')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ('taskId', 'guide', 'vehicle', 'day')

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request):
        return False

class TaskProgressInline(admin.TabularInline):
    model = TaskProgress
    extra = 0

    fields = ('task', 'checkin_time', 'checkout_time', 'checkin_long', 'checkin_lat', 'checkout_long', 'checkout_lat', 'checkin_picture', 'checkout_picture')

    raw_id_fields = ('task', )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskProgress)
class TaskProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    form = OrderForm

    confirm_template = 'admin/order/confirm.html'

    inlines = (TaskInline, TaskProgressInline, PaymentInline, BookingInline)

    fieldsets = ( 
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('orderId', 'status', 'start_time', 'end_time', 'vehicle', 'guide', 'remark')
        }),
        ('Customer Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('customer', )
        }),
        ('Company Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('company',)
        }),
        ('Charge Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('total',)
        }),
    )

    readonly_fields = (
        'orderId', 'customer', 'company', 'total'
    )

    list_display = (
       'orderId', 'status', 'customer', 'company', 'start_time', 'end_time', 'vehicle', 'guide', 'total', 'remark', 'task'
    )

    list_display_links = list_display

    raw_id_fields = (
        'guide', 'vehicle', 'company', 'customer'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'orderId', 'contact_name', 'contact_phone', 'start_time', 'end_time'
    )

    class Media:
        js = [
            'admin/js/order.js',
            'admin/js/task.js'
        ]

    def task(self, obj):
        return mark_safe("<br>".join(['%s %s %s %s'% (task.day, task.guide or '', task.vehicle or '', task.itinerary or '') for task in obj.task.all()]))

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        return False