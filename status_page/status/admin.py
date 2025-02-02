from django.contrib import admin
from .models import Service, ServiceStatus

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Removed 'status' & 'last_updated'
    search_fields = ("name",)

@admin.register(ServiceStatus)
class ServiceStatusAdmin(admin.ModelAdmin):
    list_display = ("service", "status", "updated_at")  # Now using ServiceStatus fields
    list_filter = ("status",)
    ordering = ("-updated_at",)  # Corrected field name

