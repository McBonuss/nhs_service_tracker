from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, DateTimeLocalField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    full_name = StringField('Full name', validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Create account')

class PatientForm(FlaskForm):
    nhs_number = StringField('NHS Number', validators=[DataRequired(), Length(min=10, max=12)])
    first_name = StringField('First name', validators=[DataRequired(), Length(max=80)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(max=80)])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    contact_phone = StringField('Contact phone', validators=[Optional(), Length(max=30)])
    contact_email = StringField('Contact email', validators=[Optional(), Email()])
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('discharged', 'Discharged'),
        ('deceased', 'Deceased')
    ], default='active')
    priority = SelectField('Priority', choices=[
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], default='normal')
    medical_notes = TextAreaField('Medical Notes', validators=[Optional()])
    submit = SubmitField('Save')

class PatientStatusForm(FlaskForm):
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('discharged', 'Discharged'),
        ('deceased', 'Deceased')
    ], validators=[DataRequired()])
    priority = SelectField('Priority', choices=[
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], validators=[DataRequired()])
    medical_notes = TextAreaField('Medical Notes', validators=[Optional()])
    submit = SubmitField('Update Status')

class ServiceForm(FlaskForm):
    name = StringField('Service name', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Save')

class AppointmentForm(FlaskForm):
    patient_id = SelectField('Patient', coerce=int, validators=[DataRequired()])
    service_id = SelectField('Service', coerce=int, validators=[DataRequired()])
    scheduled_for = DateTimeLocalField('Scheduled for', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=120)])
    status = SelectField('Status', choices=[('scheduled','Scheduled'),('completed','Completed'),('cancelled','Cancelled')])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save')
