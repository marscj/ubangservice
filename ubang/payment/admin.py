from django.contrib import admin

from .models import Payment
from .forms import PaymentCreatForm

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
