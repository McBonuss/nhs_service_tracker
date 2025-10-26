import click
from flask.cli import with_appcontext
from app import create_app
from app.extensions import db
from app.models import Role, User, Patient, Service, Appointment
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

app = create_app()

@app.cli.command("seed")
@with_appcontext
def seed():
    """Seed initial roles and an admin user."""
    admin = Role.query.filter_by(name='admin').first() or Role(name='admin')
    clinician = Role.query.filter_by(name='clinician').first() or Role(name='clinician')
    db.session.add_all([admin, clinician])
    db.session.commit()

    if not User.query.filter_by(email='admin@example.nhs.uk').first():
        u = User(email='admin@example.nhs.uk', full_name='Admin User', password_hash=generate_password_hash('ChangeMe123!'))
        u.roles.append(admin)
        db.session.add(u)
        db.session.commit()
        click.echo('Created admin user: admin@example.nhs.uk / ChangeMe123!')
    else:
        click.echo('Admin user already exists.')

@app.cli.command("seed-data")
@with_appcontext
def seed_data():
    """Seed comprehensive dummy data for patients, services, and appointments."""
    
    # NHS Services data
    services_data = [
        {"name": "General Practice", "description": "Primary care consultation with GP"},
        {"name": "Cardiology", "description": "Heart and cardiovascular system specialist care"},
        {"name": "Dermatology", "description": "Skin, hair, and nail conditions treatment"},
        {"name": "Orthopedics", "description": "Bone, joint, and muscle disorders treatment"},
        {"name": "Mental Health", "description": "Psychological and psychiatric care services"},
        {"name": "Physiotherapy", "description": "Physical rehabilitation and movement therapy"},
        {"name": "Radiology", "description": "Medical imaging and diagnostic scans"},
        {"name": "Blood Tests", "description": "Laboratory testing and blood work"},
        {"name": "Vaccination", "description": "Immunization and preventive care"},
        {"name": "Diabetes Care", "description": "Diabetes management and monitoring"},
        {"name": "Respiratory Care", "description": "Lung and breathing disorders treatment"},
        {"name": "Ophthalmology", "description": "Eye care and vision services"}
    ]
    
    # Create services
    for service_data in services_data:
        if not Service.query.filter_by(name=service_data["name"]).first():
            service = Service(name=service_data["name"], description=service_data["description"])
            db.session.add(service)
    
    db.session.commit()
    click.echo(f'Created {len(services_data)} NHS services.')
    
    # Patient dummy data
    patients_data = [
        {"nhs_number": "485-777-1234", "first_name": "James", "last_name": "Smith", "dob": "1985-03-15", "phone": "07700 900123", "email": "james.smith@email.com"},
        {"nhs_number": "485-777-2345", "first_name": "Emily", "last_name": "Johnson", "dob": "1992-07-22", "phone": "07700 900234", "email": "emily.johnson@email.com"},
        {"nhs_number": "485-777-3456", "first_name": "Michael", "last_name": "Williams", "dob": "1978-11-08", "phone": "07700 900345", "email": "michael.williams@email.com"},
        {"nhs_number": "485-777-4567", "first_name": "Sarah", "last_name": "Brown", "dob": "1990-01-30", "phone": "07700 900456", "email": "sarah.brown@email.com"},
        {"nhs_number": "485-777-5678", "first_name": "David", "last_name": "Jones", "dob": "1983-09-12", "phone": "07700 900567", "email": "david.jones@email.com"},
        {"nhs_number": "485-777-6789", "first_name": "Emma", "last_name": "Davis", "dob": "1995-05-18", "phone": "07700 900678", "email": "emma.davis@email.com"},
        {"nhs_number": "485-777-7890", "first_name": "Robert", "last_name": "Miller", "dob": "1970-12-03", "phone": "07700 900789", "email": "robert.miller@email.com"},
        {"nhs_number": "485-777-8901", "first_name": "Lisa", "last_name": "Wilson", "dob": "1988-04-25", "phone": "07700 900890", "email": "lisa.wilson@email.com"},
        {"nhs_number": "485-777-9012", "first_name": "Christopher", "last_name": "Moore", "dob": "1976-08-14", "phone": "07700 900901", "email": "chris.moore@email.com"},
        {"nhs_number": "485-777-0123", "first_name": "Amanda", "last_name": "Taylor", "dob": "1993-10-07", "phone": "07700 900012", "email": "amanda.taylor@email.com"},
        {"nhs_number": "485-777-1357", "first_name": "Thomas", "last_name": "Anderson", "dob": "1981-06-20", "phone": "07700 900135", "email": "thomas.anderson@email.com"},
        {"nhs_number": "485-777-2468", "first_name": "Rachel", "last_name": "Thompson", "dob": "1987-02-14", "phone": "07700 900246", "email": "rachel.thompson@email.com"},
        {"nhs_number": "485-777-3691", "first_name": "Daniel", "last_name": "White", "dob": "1979-09-28", "phone": "07700 900369", "email": "daniel.white@email.com"},
        {"nhs_number": "485-777-4825", "first_name": "Jennifer", "last_name": "Harris", "dob": "1991-12-11", "phone": "07700 900482", "email": "jennifer.harris@email.com"},
        {"nhs_number": "485-777-5936", "first_name": "Matthew", "last_name": "Clark", "dob": "1984-03-05", "phone": "07700 900593", "email": "matthew.clark@email.com"}
    ]
    
    # Create patients
    for patient_data in patients_data:
        if not Patient.query.filter_by(nhs_number=patient_data["nhs_number"]).first():
            patient = Patient(
                nhs_number=patient_data["nhs_number"],
                first_name=patient_data["first_name"],
                last_name=patient_data["last_name"],
                date_of_birth=datetime.strptime(patient_data["dob"], "%Y-%m-%d").date(),
                contact_phone=patient_data["phone"],
                contact_email=patient_data["email"]
            )
            db.session.add(patient)
    
    db.session.commit()
    click.echo(f'Created {len(patients_data)} patients.')
    
    # Create appointments
    patients = Patient.query.all()
    services = Service.query.all()
    locations = ["Room 101", "Room 102", "Room 201", "Clinic A", "Clinic B", "Ward 3", "Radiology Dept", "Lab"]
    statuses = ["scheduled", "completed", "cancelled", "no-show"]
    
    base_date = datetime.now()
    appointments_created = 0
    
    # Create appointments for the past 30 days and next 60 days
    for days_offset in range(-30, 61):
        appointment_date = base_date + timedelta(days=days_offset)
        
        # Create 1-4 appointments per day
        daily_appointments = random.randint(1, 4)
        
        for _ in range(daily_appointments):
            patient = random.choice(patients)
            service = random.choice(services)
            
            # Set appointment time (9 AM to 5 PM)
            hour = random.randint(9, 17)
            minute = random.choice([0, 15, 30, 45])
            scheduled_time = appointment_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # Status logic: past appointments are more likely to be completed
            if days_offset < 0:  # Past appointments
                status = random.choices(statuses, weights=[10, 70, 15, 5])[0]  # Mostly completed
            else:  # Future appointments
                status = random.choices(statuses, weights=[85, 5, 8, 2])[0]  # Mostly scheduled
            
            appointment = Appointment(
                patient_id=patient.id,
                service_id=service.id,
                scheduled_for=scheduled_time,
                location=random.choice(locations),
                status=status,
                notes=f"Patient appointment for {service.name}" + 
                      (f" - {random.choice(['Follow-up required', 'Regular check-up', 'Initial consultation', 'Routine screening'])}" 
                       if random.random() > 0.5 else "")
            )
            
            db.session.add(appointment)
            appointments_created += 1
    
    db.session.commit()
    click.echo(f'Created {appointments_created} appointments spanning 90 days.')
    click.echo('✅ Dummy data seeding completed successfully!')
    click.echo('📊 Summary:')
    click.echo(f'   - Services: {Service.query.count()}')
    click.echo(f'   - Patients: {Patient.query.count()}')
    click.echo(f'   - Appointments: {Appointment.query.count()}')
