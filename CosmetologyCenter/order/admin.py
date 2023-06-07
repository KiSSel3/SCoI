from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['issue']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client',
                    'created']
    list_filter = ['created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)