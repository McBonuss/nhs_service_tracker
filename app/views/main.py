from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime, timedelta
from ..models import Patient, Service, Appointment
from sqlalchemy import func

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    # Calculate dashboard statistics
    total_patients = Patient.query.count()
    active_patients = Patient.query.filter_by(status='active').count()
    high_priority_patients = Patient.query.filter_by(priority='high').count()
    urgent_patients = Patient.query.filter_by(priority='urgent').count()
    
    total_services = Service.query.count()
    
    # Appointment statistics
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    this_week = today + timedelta(days=7)
    
    today_appointments = Appointment.query.filter(
        func.date(Appointment.scheduled_for) == today,
        Appointment.status == 'scheduled'
    ).count()
    
    this_week_appointments = Appointment.query.filter(
        Appointment.scheduled_for >= datetime.now(),
        Appointment.scheduled_for <= datetime.combine(this_week, datetime.min.time()),
        Appointment.status == 'scheduled'
    ).count()
    
    total_appointments = Appointment.query.count()
    
    # Recent patients (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    recent_patients = Patient.query.filter(
        Patient.created_at >= week_ago
    ).order_by(Patient.created_at.desc()).limit(5).all()
    
    # Urgent appointments (next 24 hours)
    tomorrow_end = datetime.combine(tomorrow, datetime.max.time())
    urgent_appointments = Appointment.query.join(Patient).filter(
        Appointment.scheduled_for >= datetime.now(),
        Appointment.scheduled_for <= tomorrow_end,
        Appointment.status == 'scheduled'
    ).order_by(Appointment.scheduled_for.asc()).limit(5).all()
    
    # Patient status distribution
    status_stats = Patient.query.with_entities(
        Patient.status,
        func.count(Patient.id).label('count')
    ).group_by(Patient.status).all()
    
    # Priority distribution
    priority_stats = Patient.query.with_entities(
        Patient.priority,
        func.count(Patient.id).label('count')
    ).group_by(Patient.priority).all()
    
    return render_template('index.html',
        total_patients=total_patients,
        active_patients=active_patients,
        high_priority_patients=high_priority_patients,
        urgent_patients=urgent_patients,
        total_services=total_services,
        today_appointments=today_appointments,
        this_week_appointments=this_week_appointments,
        total_appointments=total_appointments,
        recent_patients=recent_patients,
        urgent_appointments=urgent_appointments,
        status_stats=dict(status_stats),
        priority_stats=dict(priority_stats)
    )
