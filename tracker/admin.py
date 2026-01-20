from django.contrib import admin
from .models import Patient, Service, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("nhs_number", "first_name", "last_name", "status", "priority")
    search_fields = ("nhs_number", "first_name", "last_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "service", "scheduled_for", "status")
    list_filter = ("status", "service")
