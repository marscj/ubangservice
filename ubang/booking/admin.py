from django.contrib import admin
from django.utils.safestring import mark_safe
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from functools import update_wrapper
from django.core.exceptions import ValidationError

from .models import Booking, Itinerary
from .forms import ItineraryInlineFormSet

class BookingInline(admin.TabularInline): 
    model = Booking 
    extra = 0 
    fk_name = 'order'

    exclude = (
        'pick_up_addr', 'drop_off_addr', 'remark', 
    )

    readonly_fields = (
        'bookingId',
    )

    def has_delete_permission(self, request, obj):
        return False
    
    def has_add_permission(self, request):
        return False
  

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 0
    formset = ItineraryInlineFormSet

    fields = ('day', 'itinerary', 'remark')

    # readonly_fields = ('day', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ('taskId', 'guide', 'vehicle', 'day')

    # def has_delete_permission(self, request, obj):
    #     return False

    # def has_add_permission(self, request):
    #     return False

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    inlines = (
        ItineraryInline,
    )

    list_display = (
        'bookingId', 'start_time', 'end_time', 'vehicle', 'guide', 'contact_name', 'contact_phone', 'itinerary'
    )
    
    def itinerary(self, obj):
        return mark_safe("<br>".join(['%s %s'% (itinerary.day,  itinerary.itinerary or '') for itinerary in obj.itinerary.all()]))

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     obj = Order.objects.get(pk=object_id)
    #     extra_context = {
    #         'show_confirm': obj.status == OrderStatus.Draft, 
    #         'show_cancel': obj.status == OrderStatus.Confirm
    #     }
    #     return super().change_view(request, object_id, form_url, extra_context)

    # def get_urls(self):
    #     from django.urls import path

    #     def wrap(view):
    #         def wrapper(*args, **kwargs):
    #             return self.admin_site.admin_view(view)(*args, **kwargs)
    #         wrapper.model_admin = self
    #         return update_wrapper(wrapper, view)

    #     info = self.model._meta.app_label, self.model._meta.model_name

    #     urlpatterns = [
    #         path('<path:object_id>/confirm/', wrap(self.confirm_view), name='%s_%s_confirm' % info),
    #     ]

    #     urls = urlpatterns + super().get_urls()
    #     return urls
    
    # def confirm_view(self, request, object_id, form_url='',extra_context=None):
        
    #     opts = self.model._meta
    #     obj = Order.objects.get(pk=object_id)
    
    #     if request.POST:
    #         return self.response_confirm(request, obj)
        
    #     context = {
    #         'opts': opts, 
    #         'object': obj,
    #         'show_confirm': obj.status == OrderStatus.Draft, 
    #         'show_cancel': obj.status == OrderStatus.Confirm
    #     }
    #     return render(request, self.confirm_template, context)

    # def response_confirm(self, request, obj):

    #     opts = self.model._meta
    #     preserved_filters = self.get_preserved_filters(request)

    #     if 'confirm' in request.POST:
    #         obj.confirm()
    #         list(messages.get_messages(request))
    #         self.message_user(request, 'The Order %s was confirmed' % obj.orderId)
            
    #     elif 'cancel' in request.POST:
    #         obj.cancel()
    #         list(messages.get_messages(request))
    #         self.message_user(request, 'The Order %s was cancelled' % obj.orderId, messages.WARNING)

    #     redirect_url = reverse('admin:%s_%s_change' %
    #                                (opts.app_label, opts.model_name),
    #                                args=(obj.pk,),
    #                                current_app=self.admin_site.name)

    #     redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
    #     return HttpResponseRedirect(redirect_url)

