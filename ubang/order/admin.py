from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from functools import update_wrapper


from datetime import datetime

from .models import Order
from .forms import OrderForm
from .import OrderStatus
from ubang.task.admin import TaskInline, TaskPriceInline, TaskProgressInline
from ubang.payment.admin import PaymentInline

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    form = OrderForm

    confirm_template = 'admin/order/confirm.html'

    inlines = (TaskInline, TaskPriceInline, TaskProgressInline, PaymentInline, )

    fieldsets = ( 
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': ('orderId', 'status', 'contact_name', 'contact_phone', 'arrival_time', 'departure_time', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 'link', 'remark')
        }),
        ('Charge Info', {
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
       'orderId', 'status', 'create_by', 'contact_name', 'contact_phone', 'arrival_time', 'departure_time', 'vehicle', 'guide', 'pick_up_addr', 'drop_off_addr', 'discount_name', 'total', 'remark', 'hyper_link', 'tasks'
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

    class Media:
        js = [
            'admin/js/order.js'
        ]

    def hyper_link(self, obj):
        return format_html("<a href='{0}'>{0}</a>", obj.link)

    hyper_link.short_description = 'Hyperlink'

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

    def save_model(self, request, obj, form, change):

        if obj.status == OrderStatus.Draft:
            messages.warning(request, 'You have only 2 hours to confirm the order, it will expire')

        return super().save_model(request, obj, form, change)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = Order.objects.get(pk=object_id)
        extra_context = {
            'show_confirm': obj.status == OrderStatus.Draft, 
            'show_cancel': obj.status == OrderStatus.Confirm
        }
        return super().change_view(request, object_id, form_url, extra_context)

    def get_urls(self):
        from django.urls import path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        urlpatterns = [
            path('<path:object_id>/confirm/', wrap(self.confirm_view), name='%s_%s_confirm' % info),
        ]

        urls = urlpatterns + super().get_urls()
        return urls
    
    def confirm_view(self, request, object_id, form_url='',extra_context=None):
        
        opts = self.model._meta
        obj = Order.objects.get(pk=object_id)
    
        if request.POST:
            return self.response_confirm(request, obj)
        
        context = {
            'opts': opts, 
            'object': obj,
            'show_confirm': obj.status == OrderStatus.Draft, 
            'show_cancel': obj.status == OrderStatus.Confirm
        }
        return render(request, self.confirm_template, context)

    def response_confirm(self, request, obj):

        opts = self.model._meta
        preserved_filters = self.get_preserved_filters(request)

        if 'confirm' in request.POST:
            obj.confirm()
            list(messages.get_messages(request))
            self.message_user(request, 'The Order %s was confirmed' % obj.orderId)
            
        elif 'cancel' in request.POST:
            obj.cancel()
            list(messages.get_messages(request))
            self.message_user(request, 'The Order %s was cancelled' % obj.orderId, messages.WARNING)

        redirect_url = reverse('admin:%s_%s_change' %
                                   (opts.app_label, opts.model_name),
                                   args=(obj.pk,),
                                   current_app=self.admin_site.name)

        redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
        return HttpResponseRedirect(redirect_url)

    def tasks(self, obj):
        return mark_safe("<br>".join(['%s %s %s %s'% (task.day, task.guide or '', task.vehicle or '', task.itinerary or '') for task in obj.task.all()]))