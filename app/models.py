from datetime import datetime
from .extensions import db
from flask_login import UserMixin

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.relationship('Role', secondary=roles_users, backref='users')

    def has_role(self, role_name):
        return any(r.name == role_name for r in self.roles)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nhs_number = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_phone = db.Column(db.String(30), nullable=True)
    contact_email = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(20), default="active")  # active, inactive, discharged, deceased
    priority = db.Column(db.String(20), default="normal")  # low, normal, high, urgent
    medical_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    appointments = db.relationship('Appointment', backref='patient', cascade="all, delete-orphan")

    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    @property
    def next_appointment(self):
        from datetime import datetime
        return self.appointments.filter(
            Appointment.scheduled_for > datetime.now(),
            Appointment.status == 'scheduled'
        ).order_by(Appointment.scheduled_for.asc()).first()
    
    @property
    def total_appointments(self):
        return len(self.appointments)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    scheduled_for = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), default="scheduled")
    notes = db.Column(db.Text, nullable=True)
    service = db.relationship('Service')
