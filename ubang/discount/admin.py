from django.contrib import admin

from .models import Discount

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass
