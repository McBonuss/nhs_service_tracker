#!/usr/bin/env python3
"""
Quick verification script for the NHS Service Tracker dummy data (Django).
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nhs_service_tracker.settings")
django.setup()

from tracker.models import Patient, Service, Appointment


def main():
    print("=== NHS Service Tracker Database Summary ===")
    print(f"Services: {Service.objects.count()}")
    print(f"Patients: {Patient.objects.count()}")
    print(f"Appointments: {Appointment.objects.count()}")

    print("\n=== Sample Services ===")
    for service in Service.objects.all()[:5]:
        print(f"  - {service.name}: {service.description}")

    print("\n=== Sample Patients ===")
    for patient in Patient.objects.all()[:5]:
        print(f"  - {patient.first_name} {patient.last_name} (NHS: {patient.nhs_number})")

    print("\n=== Recent Appointments ===")
    for appointment in Appointment.objects.select_related("patient", "service")[:5]:
        print(
            f"  - {appointment.patient.first_name} {appointment.patient.last_name} -> {appointment.service.name}"
        )
        print(f"    Scheduled: {appointment.scheduled_for:%Y-%m-%d %H:%M}")
        print(f"    Status: {appointment.status}")
        print()


if __name__ == "__main__":
    main()