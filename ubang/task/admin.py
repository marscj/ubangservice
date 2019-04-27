from django.contrib import admin

from .models import Task, TaskPrice, TaskProgress
from .forms import TaskInlineFormSet

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    formset = TaskInlineFormSet
    
    fields = ('taskId', 'day', 'itinerary', 'guide', 'vehicle', 'remark')

    raw_id_fields = ('vehicle', 'guide', )

    readonly_fields = ('taskId',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ('taskId', 'guide', 'vehicle', 'day')

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request):
        return False

class TaskPriceInline(admin.TabularInline):
    model = TaskPrice
    extra = 0

    fields = ('__str__', 'total_gross', 'discount_name', 'extra', 'total', 'description')

    raw_id_fields = ('task', )

    readonly_fields = ('__str__', 'total_gross', 'total', 'discount_name')

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

