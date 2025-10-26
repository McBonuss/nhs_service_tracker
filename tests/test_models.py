from app.extensions import db
from app.models import Patient, Service, Appointment
from datetime import datetime

def test_create_patient(app):
    p = Patient(nhs_number='1234567890', first_name='Jane', last_name='Doe', date_of_birth=datetime(1990,1,1))
    db.session.add(p); db.session.commit()
    assert p.id is not None

def test_appointment_relations(app):
    s = Service(name='Cardiology')
    p = Patient(nhs_number='1234567891', first_name='John', last_name='Smith', date_of_birth=datetime(1985,5,5))
    db.session.add_all([s,p]); db.session.commit()
    a = Appointment(patient_id=p.id, service_id=s.id, scheduled_for=datetime(2030,1,1,9,0), location='Clinic A')
    db.session.add(a); db.session.commit()
    assert a.patient.last_name == 'Smith'
    assert a.service.name == 'Cardiology'
