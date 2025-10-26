from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from ..extensions import db
from ..models import Service
from ..forms import ServiceForm
from ..security import roles_required

services_bp = Blueprint('services', __name__)

@services_bp.route('/')
@login_required
def list():
    services = Service.query.order_by(Service.name).all()
    return render_template('services/list.html', services=services)

@services_bp.route('/create', methods=['GET','POST'])
@login_required
@roles_required('admin')
def create():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(name=form.name.data.strip(), description=form.description.data)
        db.session.add(service)
        db.session.commit()
        flash('Service created.', 'success')
        return redirect(url_for('services.list'))
    return render_template('services/form.html', form=form, mode="Create")

@services_bp.route('/<int:id>/edit', methods=['GET','POST'])
@login_required
@roles_required('admin')
def edit(id):
    service = Service.query.get_or_404(id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        form.populate_obj(service)
        db.session.commit()
        flash('Service updated.', 'success')
        return redirect(url_for('services.list'))
    return render_template('services/form.html', form=form, mode="Edit")

@services_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
@roles_required('admin')
def delete(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    flash('Service deleted.', 'info')
    return redirect(url_for('services.list'))
