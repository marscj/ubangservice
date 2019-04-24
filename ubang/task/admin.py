from django.contrib import admin

from .models import Task, TaskPrice, TaskProgress
from .forms import TaskInlineFormSet

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    formset = TaskInlineFormSet
    
    fields = ('taskId', 'day', 'itinerary', 'guide', 'vehicle', 'remark')

    raw_id_fields = ('itinerary', 'vehicle', 'guide', )

    readonly_fields = ('taskId',)

class TaskPriceInline(admin.TabularInline):
    model = TaskPrice
    extra = 0

    fields = ('__str__', 'type', 'total_gross', 'discount_name', 'extra', 'total', 'description')

    raw_id_fields = ('task', )

    readonly_fields = ('__str__', 'total_gross', 'total', 'type', 'discount_name')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj):
        return False

class TaskProgressInline(admin.TabularInline):
    model = TaskProgress
    extra = 0

    fields = ('task', 'checkin_time', 'checkout_time', 'checkin_long', 'checkin_lat', 'checkout_long', 'checkout_lat', 'checkin_picture', 'checkout_picture')

    raw_id_fields = ('task', )
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskPrice)
class TaskPriceAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskProgress)
class TaskProgressAdmin(admin.ModelAdmin):
    pass

