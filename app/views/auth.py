from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from ..forms import LoginForm, RegisterForm
from ..models import User, Role

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Signed in successfully.', 'success')
            next_url = request.args.get('next') or url_for('main.index')
            return redirect(next_url)
        flash('Invalid credentials.', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash('Email already registered.', 'warning')
        else:
            user = User(
                email=form.email.data.lower(),
                full_name=form.full_name.data,
                password_hash=generate_password_hash(form.password.data)
            )
            clinician = Role.query.filter_by(name="clinician").first()
            if not clinician:
                clinician = Role(name="clinician")
                db.session.add(clinician)
            user.roles.append(clinician)
            db.session.add(user)
            db.session.commit()
            flash('Account created. You can sign in now.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Signed out.', 'info')
    return redirect(url_for('auth.login'))
