import pytest
from django.utils import timezone

from tracker.models import Appointment, Patient, Service


@pytest.mark.django_db
def test_create_patient():
    p = Patient.objects.create(
        nhs_number="1234567890",
        first_name="Jane",
        last_name="Doe",
        date_of_birth=timezone.datetime(1990, 1, 1).date(),
    )
    assert p.id is not None


@pytest.mark.django_db
def test_appointment_relations():
    s = Service.objects.create(name="Cardiology")
    p = Patient.objects.create(
        nhs_number="1234567891",
        first_name="John",
        last_name="Smith",
        date_of_birth=timezone.datetime(1985, 5, 5).date(),
    )
    a = Appointment.objects.create(
        patient=p,
        service=s,
        scheduled_for=timezone.make_aware(timezone.datetime(2030, 1, 1, 9, 0)),
        location="Clinic A",
    )
    assert a.patient.last_name == "Smith"
    assert a.service.name == "Cardiology"
