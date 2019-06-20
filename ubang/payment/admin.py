from django.contrib import admin

from .models import Payment
from .forms import PaymentCreatForm

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

    fields =(
        'charge_status', 'total', 'captured_amount', 'currency', 'remark'
    )

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
    
#     form = PaymentCreatForm

#     readonly_fields = (
#         'token',
#     )
