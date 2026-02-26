# NHS Service Tracker

A Django web application for managing NHS patients, services, and appointments. Built for healthcare teams to track care workflows, priorities, and appointments in a single, secure system.

## Table of Contents

- [Overview](#overview)
- [UX](#ux)
- [Wireframes](#wireframes)
- [Features](#features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security](#security)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Overview

### Purpose & Value

The NHS Service Tracker provides:

- Enhanced patient management
- Patient status tracking (Active, Inactive, Discharged, Deceased)
- Priority management (Low, Medium, High, Urgent)
- Advanced dashboard metrics
- Service management
- Appointment scheduling
- Secure authentication
- Modern responsive NHS-style design

This project solves operational fragmentation in small NHS clinics by consolidating patients, services, and appointments into a single, secure system.

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

- Enhanced patient records with NHS number tracking
- Patient status management
- Priority levels with color-coded badges
- Advanced dashboard analytics
- Appointment scheduling system
- Service management module
- Secure Django authentication
- Search and filter across entities
- Responsive NHS-style UI

### Enhanced Features

- Real-time patient status distribution
- Calculated fields (age, next appointment)
- Interactive card-based dashboard
- Data validation and secure form handling

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
- JavaScript (vanilla)

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
- Security checks

Run tests:

```bash
pytest
pytest --cov=tracker
```

Manual testing is documented in [TEST_PLAN.md](TEST_PLAN.md).

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
python manage.py runserver
```

### Heroku Deployment

```bash
heroku create app-name
heroku addons:create heroku-postgresql:essential-0
heroku config:set SECRET_KEY="<your-secret-key>"
heroku config:set DEBUG=0

git push heroku main
heroku run python manage.py migrate
```

## Security

- Django authentication
- CSRF protection
- Password hashing
- `login_required` decorators
- ORM SQL injection protection
- Environment-based `SECRET_KEY` storage

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
