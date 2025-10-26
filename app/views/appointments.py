from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from ..extensions import db
from ..models import Appointment, Patient, Service
from ..forms import AppointmentForm
from ..security import roles_required

appointments_bp = Blueprint('appointments', __name__)

def _choices(form):
    form.patient_id.choices = [(p.id, f"{p.last_name}, {p.first_name} ({p.nhs_number})") for p in Patient.query.order_by(Patient.last_name).all()]
    form.service_id.choices = [(s.id, s.name) for s in Service.query.order_by(Service.name).all()]

@appointments_bp.route('/')
@login_required
def list():
    q = request.args.get('q','')
    appts = Appointment.query.join(Patient).join(Service)
    if q:
        like = f"%{q.lower()}%"
        appts = appts.filter(
            db.or_(Patient.last_name.ilike(like), Service.name.ilike(like))
        )
    appts = appts.order_by(Appointment.scheduled_for.desc()).all()
    return render_template('appointments/list.html', appointments=appts, q=q)

@appointments_bp.route('/create', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def create():
    form = AppointmentForm()
    _choices(form)
    if form.validate_on_submit():
        appt = Appointment(
            patient_id=form.patient_id.data,
            service_id=form.service_id.data,
            scheduled_for=form.scheduled_for.data,
            location=form.location.data.strip(),
            status=form.status.data,
            notes=form.notes.data
        )
        db.session.add(appt)
        db.session.commit()
        flash('Appointment created.', 'success')
        return redirect(url_for('appointments.list'))
    return render_template('appointments/form.html', form=form, mode="Create")

@appointments_bp.route('/<int:id>/edit', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def edit(id):
    appt = Appointment.query.get_or_404(id)
    form = AppointmentForm(obj=appt)
    _choices(form)
    if form.validate_on_submit():
        form.populate_obj(appt)
        db.session.commit()
        flash('Appointment updated.', 'success')
        return redirect(url_for('appointments.list'))
    return render_template('appointments/form.html', form=form, mode="Edit")

@appointments_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
@roles_required('admin')
def delete(id):
    appt = Appointment.query.get_or_404(id)
    db.session.delete(appt)
    db.session.commit()
    flash('Appointment deleted.', 'info')
    return redirect(url_for('appointments.list'))
