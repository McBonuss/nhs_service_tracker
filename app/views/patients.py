from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from ..extensions import db
from ..models import Patient
from ..forms import PatientForm
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
            contact_email=form.contact_email.data or None
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient created.', 'success')
        return redirect(url_for('patients.list'))
    return render_template('patients/form.html', form=form, mode="Create")

@patients_bp.route('/<int:id>/edit', methods=['GET','POST'])
@login_required
@roles_required('admin','clinician')
def edit(id):
    patient = Patient.query.get_or_404(id)
    form = PatientForm(obj=patient)
    if form.validate_on_submit():
        form.populate_obj(patient)
        db.session.commit()
        flash('Patient updated.', 'success')
        return redirect(url_for('patients.list'))
    return render_template('patients/form.html', form=form, mode="Edit")

@patients_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
@roles_required('admin')
def delete(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient deleted.', 'info')
    return redirect(url_for('patients.list'))
