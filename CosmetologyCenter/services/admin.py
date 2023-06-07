from django.contrib import admin
from .models import Device,Issue
# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(Issue)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['issue_type', 'device_type', 'price']
