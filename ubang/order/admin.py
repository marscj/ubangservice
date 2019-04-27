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

    class Media:
        js = [
            'admin/js/order.js'
        ]
    
    form = OrderForm

    inlines = (TaskInline, TaskPriceInline, TaskProgressInline, PaymentInline, )

    fieldsets = ( 
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('orderId', 'status', 'contact_name', 'contact_phone', 'arrival_time', 'departure_time', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 'link', 'remark')
        }),
        ('Price Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('discount_name', 'total',)
        }),
        ('Customer Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('create_by', 'customer_name', 'customer_phone', 'customer_company', 'customer_company_phone', 'customer_company_tel', 'customer_company_address', 'customer_company_discount')
        }),
        ('Create Info', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('create_at', 'change_at')
        })
    )

    add_fieldsets = ( 
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('contact_name', 'contact_phone', 'arrival_time', 'departure_time', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 'link', 'remark')
        }),
    )

    list_display = (
       'orderId', 'status', 'create_by', 'contact_name', 'contact_phone', 'arrival_time', 'departure_time', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 'discount_name', 'total', 'remark', 'hyper_link'
    )

    list_display_links = list_display

    raw_id_fields = (
        'create_by', 'guide', 'vehicle',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'orderId', 'contact_name', 'contact_phone', 'arrival_time', 'departure_time'
    )

    readonly_fields = (
        'orderId', 'create_at', 'change_at', 'discount_name', 'total', 'hyper_link', 'create_by', 'customer_name', 'customer_phone', 'customer_company', 'customer_company_phone', 'customer_company_tel', 'customer_company_address', 'customer_company_discount'
    )

    def hyper_link(self, obj):
        return format_html("<a href='{0}'>{0}</a>", obj.link)

    hyper_link.short_description = 'Hyperlink'

    #  def project_contacts(self):
    #        try:
    #        return ",".join(map(lambda c: c.name ,  self.project.contact.all()))
    #    except Exception, e : 
    #        return "Error:%s" % str(e)

    def get_fieldsets(self, request, obj=None):
        if obj == None:
            return self.add_fieldsets
        else:
            return super().get_fieldsets(request, obj)

    def get_inline_instances(self, request, obj=None):
        if obj == None:
            return ()
        else:
            return super().get_inline_instances(request, obj)