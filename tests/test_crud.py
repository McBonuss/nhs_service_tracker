from datetime import date
import pytest
from tracker.models import Appointment, Patient, Service


@pytest.mark.django_db
def test_patient_crud(client, user):
    assert client.login(username=user.username, password="ChangeMe123!")

    rv = client.post(
        "/patients/add/",
        data={
            "nhs_number": "9990001111",
            "first_name": "Alice",
            "last_name": "Brown",
            "date_of_birth": "1991-02-03",
            "contact_email": "alice@example.com",
            "status": "active",
            "priority": "medium",
        },
        follow=True,
    )
    assert b"Patient created." in rv.content

    rv = client.get("/patients/?q=Brown")
    assert b"Brown" in rv.content

    patient = Patient.objects.get(nhs_number="9990001111")
    rv = client.post(
        f"/patients/{patient.id}/edit/",
        data={
            "nhs_number": "9990001111",
            "first_name": "Alice",
            "last_name": "Green",
            "date_of_birth": "1991-02-03",
            "contact_email": "alice@example.com",
            "status": "inactive",
            "priority": "high",
        },
        follow=True,
    )
    assert b"Patient updated." in rv.content

    rv = client.post(f"/patients/{patient.id}/delete/", follow=True)
    assert b"Patient deleted." in rv.content


@pytest.mark.django_db
def test_service_crud(client, user):
    assert client.login(username=user.username, password="ChangeMe123!")

    rv = client.post(
        "/services/add/",
        data={"name": "Neurology", "description": "Neurology services"},
        follow=True,
    )
    assert b"Service created." in rv.content

    service = Service.objects.get(name="Neurology")
    rv = client.post(
        f"/services/{service.id}/edit/",
        data={"name": "Neurology", "description": "Brain and nerve care"},
        follow=True,
    )
    assert b"Service updated." in rv.content

    rv = client.post(f"/services/{service.id}/delete/", follow=True)
    assert b"Service deleted." in rv.content


@pytest.mark.django_db
def test_appointment_crud(client, user):
    assert client.login(username=user.username, password="ChangeMe123!")

    patient = Patient.objects.create(
        nhs_number="8880001111",
        first_name="Sam",
        last_name="Jones",
        date_of_birth=date(1988, 1, 1),
    )
    service = Service.objects.create(name="Oncology", description="Cancer care")

    rv = client.post(
        "/appointments/add/",
        data={
            "patient": patient.id,
            "service": service.id,
            "scheduled_for": "2030-01-01T09:30",
            "location": "Room 5",
            "status": "scheduled",
            "notes": "Initial consult",
        },
        follow=True,
    )
    assert b"Appointment created." in rv.content

    appointment = Appointment.objects.get(patient=patient, service=service)
    rv = client.post(
        f"/appointments/{appointment.id}/edit/",
        data={
            "patient": patient.id,
            "service": service.id,
            "scheduled_for": "2030-01-02T10:00",
            "location": "Room 7",
            "status": "completed",
            "notes": "Follow-up",
        },
        follow=True,
    )
    assert b"Appointment updated." in rv.content

    rv = client.post(f"/appointments/{appointment.id}/delete/", follow=True)
    assert b"Appointment deleted." in rv.content
