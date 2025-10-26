from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from datetime import datetime
from ..extensions import db
from ..models import Patient, Appointment
from ..forms import PatientForm, PatientStatusForm
from ..security import roles_required

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/')
@login_required
def list():
    q = request.args.get('q','')
    patients = Patient.query
    if q:
        like = f"%{q.lower()}%"
        patients = patients.filter(
            db.or_(Patient.first_name.ilike(like), Patient.last_name.ilike(like), Patient.nhs_number.ilike(like))
        )
    return render_template('patients/list.html', patients=patients.order_by(Patient.last_name).all(), q=q)

@patients_bp.route('/create', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def create():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(
            nhs_number=form.nhs_number.data.strip(),
            first_name=form.first_name.data.strip(),
            last_name=form.last_name.data.strip(),
            date_of_birth=form.date_of_birth.data,
            contact_phone=form.contact_phone.data or None,
            contact_email=form.contact_email.data or None,
            status=form.status.data,
            priority=form.priority.data,
            medical_notes=form.medical_notes.data
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient created successfully.', 'success')
        return redirect(url_for('patients.detail', id=patient.id))
    return render_template('patients/form.html', form=form, mode="Create")

@patients_bp.route('/<int:id>/edit', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def edit(id):
    patient = Patient.query.get_or_404(id)
    form = PatientForm(obj=patient)
    if form.validate_on_submit():
        patient.nhs_number = form.nhs_number.data.strip()
        patient.first_name = form.first_name.data.strip()
        patient.last_name = form.last_name.data.strip()
        patient.date_of_birth = form.date_of_birth.data
        patient.contact_phone = form.contact_phone.data or None
        patient.contact_email = form.contact_email.data or None
        patient.status = form.status.data
        patient.priority = form.priority.data
        patient.medical_notes = form.medical_notes.data
        patient.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Patient updated successfully.', 'success')
        return redirect(url_for('patients.detail', id=id))
    return render_template('patients/form.html', form=form, mode="Edit", patient=patient)

@patients_bp.route('/<int:id>')
@login_required
def detail(id):
    patient = Patient.query.get_or_404(id)
    
    # Get recent appointments
    recent_appointments = Appointment.query.filter_by(patient_id=id)\
        .order_by(Appointment.scheduled_for.desc()).limit(10).all()
    
    # Get next appointment
    next_appointment = Appointment.query.filter(
        Appointment.patient_id == id,
        Appointment.scheduled_for > datetime.now(),
        Appointment.status == 'scheduled'
    ).order_by(Appointment.scheduled_for.asc()).first()
    
    return render_template('patients/detail.html', 
                         patient=patient, 
                         recent_appointments=recent_appointments,
                         next_appointment=next_appointment)

@patients_bp.route('/<int:id>/status', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def edit_status(id):
    patient = Patient.query.get_or_404(id)
    form = PatientStatusForm(obj=patient)
    if form.validate_on_submit():
        patient.status = form.status.data
        patient.priority = form.priority.data
        patient.medical_notes = form.medical_notes.data
        patient.updated_at = datetime.utcnow()
        db.session.commit()
        flash(f'Patient status updated to {patient.status.title()}.', 'success')
        return redirect(url_for('patients.detail', id=id))
    return render_template('patients/status_form.html', form=form, patient=patient)

@patients_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
@roles_required('admin')
def delete(id):
    patient = Patient.query.get_or_404(id)
    patient_name = f"{patient.first_name} {patient.last_name}"
    db.session.delete(patient)
    db.session.commit()
    flash(f'Patient {patient_name} has been deleted.', 'info')
    return redirect(url_for('patients.list'))
