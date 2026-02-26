# NHS Service Tracker

A Django web application for managing NHS patients, services, and appointments. Built for healthcare teams to track care workflows, priorities, and appointments in a single, secure system.

## Table of Contents

- [Overview](#overview)
- [Rationale](#rationale)
- [UX](#ux)
- [Wireframes](#wireframes)
- [Features](#features)
- [Data Model](#data-model)
- [Code Snippets](#code-snippets)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security](#security)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Overview

### Purpose & Value

The NHS Service Tracker provides:

- Patient management with status and priority fields
- Dashboard totals for patients, services, and appointments
- Service management
- Appointment scheduling
- Secure authentication
- Responsive NHS-style design

This project consolidates patients, services, and appointments into a single system so staff can manage care workflows without spreadsheets or disconnected notes.

## Rationale

- Clinics often rely on spreadsheets for patient lists and appointments, which makes updates inconsistent and auditing difficult.
- This app keeps core data in a relational structure so patient status and appointment history stay linked.
- The dashboard provides a quick operational snapshot to reduce time spent gathering totals.

Design decisions were focused on clarity, speed of access, and reduced risk of data entry errors.

### Requirements

- Python 3.8+
- Django 5+
- SQLite (development) or PostgreSQL (production)
- Modern web browser

### Project Structure

```plaintext
nhs_service_tracker/
├── nhs_service_tracker/          # Django project package
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
├── tracker/                      # Django app (views, models, forms)
├── templates/                    # Django templates
├── static/                       # Static assets (CSS/JS)
├── tests/                       # Test suite
├── docs/                        # Documentation (wireframes)
├── manage.py                    # CLI commands and data seeding
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment configuration
└── README.md                    # Project documentation
```

## UX

### Target Audience

- Reception/admin staff
- Clinicians
- Service managers/supervisors

### User Stories

- As a receptionist, I can create a patient record.
- As a clinician, I can update medical notes.
- As an admin, I can manage services.
- As a scheduler, I can book and manage appointments.
- As a manager, I can view workload statistics.

### Design Principles

- Clean, scannable interface
- NHS-inspired color palette
- Clear information hierarchy
- Accessible forms and navigation
- Dashboard-first information design

## Wireframes

Wireframes were created during the planning phase to define layout, functionality, and user journeys before development began. The mockups cover:

- Dashboard statistics layout
- Patient list view
- Patient detail view
- Appointment booking form
- Service management table
- Responsive layout across devices

Wireframe notes are documented in [docs/wireframes/README.md](docs/wireframes/README.md).

![Wireframes](docs/wireframes/wire_frames.png)

## Features

### Core Functionality

- Patient records with NHS number tracking
- Patient status and priority management
- Dashboard summary cards
- Appointment scheduling
- Service management
- Secure Django authentication
- Patient search by name or NHS number
- Responsive NHS-style UI

### Additional Features

- Calculated fields (age, next appointment)
- Confirmation step for delete actions
- Data validation and secure form handling
- Dashboard status distribution and priority badges

## Data Model

### Patients

- NHS number (unique)
- Demographics
- Status (Active, Inactive, Discharged, Deceased)
- Priority (Low, Medium, High, Urgent)
- Medical notes
- Calculated age
- Appointment history

### Services

- Service name
- Description
- Linked appointments

### Appointments

- Linked patient
- Linked service
- Date/time
- Location
- Status
- Notes

Relationships allow:

- Dashboard summaries
- Upcoming appointment tracking
- Priority distribution analytics

### Seeded Data (Optional)

- Example services (General Practice, Cardiology, Mental Health, etc.)
- Sample patients with realistic NHS numbers and contact data
- Example appointments across past and upcoming dates

## Code Snippets

### Model Relationships

```python
class Appointment(models.Model):
	patient = models.ForeignKey(Patient, related_name="appointments", on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	scheduled_for = models.DateTimeField()
	location = models.CharField(max_length=120)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
```

### Protected CRUD View

```python
@login_required
def patients_edit(request, pk):
	patient = get_object_or_404(Patient, pk=pk)
	form = PatientForm(request.POST or None, instance=patient)
	if request.method == "POST" and form.is_valid():
		form.save()
		messages.success(request, "Patient updated.")
		return redirect("patients_detail", pk=patient.pk)
	return render(request, "patients/form.html", {"form": form, "title": "Edit Patient"})
```

### Template Form Pattern

```html
<form method="post" novalidate>
  {% csrf_token %}
  {{ form.non_field_errors }}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

## Technologies Used

### Backend

- Python 3.8+
- Django 5+
- SQLite (development)
- PostgreSQL (production)
- Gunicorn

### Frontend

- HTML5
- CSS3 (custom)

### Testing & Quality

- pytest
- pytest-django
- coverage
- flake8

## Testing

### Automated Tests

- Authentication flows
- CRUD operations
- Model validation
- Security checks for protected routes

Run tests:

```bash
pytest
pytest --cov=tracker
```

Manual testing is documented in [TEST_PLAN.md](TEST_PLAN.md).

### Running Specific Tests

```bash
pytest tests/test_auth_routes.py
pytest tests/test_models.py
pytest tests/test_crud.py
```

## Deployment

### Local Setup

```bash
python -m venv .venv
# Activate the venv, then
pip install -r requirements.txt
copy env.example env  # Windows
# cp env.example env  # macOS/Linux
python manage.py migrate
python manage.py seed
python manage.py seed_data
python manage.py runserver
```

### Default Login Credentials

- Email: admin@example.nhs.uk
- Password: ChangeMe123!

### Heroku Deployment

```bash
heroku create app-name
heroku addons:create heroku-postgresql:essential-0
heroku config:set SECRET_KEY="<your-secret-key>"
heroku config:set DEBUG=0

git push heroku main
heroku run python manage.py migrate
```

### One-click Deploy

The included app.json supports Heroku setup with automatic database creation and migrations. After creating the app, set a production SECRET_KEY and run migrations if needed.

## Security

- Django authentication
- CSRF protection
- Password hashing
- `login_required` decorators on CRUD routes
- ORM SQL injection protection
- Environment-based `SECRET_KEY` storage
- Set DEBUG=0 in production

## Future Enhancements

- Calendar view integration
- Email reminders
- Mobile app
- REST API endpoints
- NHS Spine integration
- Audit logging
- Advanced reporting

## Credits

- Wireframes created by the developer
- NHS design inspiration from NHS Digital guidelines
- Django documentation
- Code Institute learning materials
