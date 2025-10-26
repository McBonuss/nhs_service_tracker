#!/usr/bin/env python3
"""
Quick verification script for the NHS Service Tracker dummy data.
"""

from app import create_app
from app.models import Patient, Service, Appointment

def main():
    app = create_app()
    with app.app_context():
        print("=== NHS Service Tracker Database Summary ===")
        print(f"Services: {Service.query.count()}")
        print(f"Patients: {Patient.query.count()}")
        print(f"Appointments: {Appointment.query.count()}")
        
        print("\n=== Sample Services ===")
        for service in Service.query.limit(5):
            print(f"  - {service.name}: {service.description}")
        
        print("\n=== Sample Patients ===")
        for patient in Patient.query.limit(5):
            print(f"  - {patient.first_name} {patient.last_name} (NHS: {patient.nhs_number})")
        
        print("\n=== Recent Appointments ===")
        for appointment in Appointment.query.limit(5):
            print(f"  - {appointment.patient.first_name} {appointment.patient.last_name} -> {appointment.service.name}")
            print(f"    Scheduled: {appointment.scheduled_for.strftime('%Y-%m-%d %H:%M')}")
            print(f"    Status: {appointment.status}")
            print()

if __name__ == "__main__":
    main()