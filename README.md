# NHS Service Tracker

A comprehensive Django web application for managing NHS patients, services, and appointments. Built with modern web technologies and designed for healthcare professionals to efficiently track and manage patient care workflows with enhanced patient status management and detailed analytics.

## 🏥 Overview

The NHS Service Tracker is a full-featured healthcare management system that provides:

- **Enhanced Patient Management**: Complete patient records with NHS numbers, demographics, contact information, status tracking, priority levels, and medical notes
- **Patient Status Management**: Comprehensive status tracking (Active, Inactive, Discharged, Deceased) with priority levels (Low, Medium, High, Urgent)
- **Advanced Dashboard**: Real-time statistics showing patient counts, appointment summaries, service usage, and recent activity
- **Service Management**: Comprehensive NHS service catalog (Cardiology, Mental Health, GP services, etc.)
- **Appointment Scheduling**: Advanced booking system with status tracking and location management
- **User Authentication**: Secure Django authentication for staff and admin users
- **Search & Filtering**: Powerful search functionality across all entities
- **Modern Responsive Design**: Professional NHS-compliant interface with mobile-friendly design

## 🎯 Purpose & Value

The app helps healthcare staff keep patient, service, and appointment data in one place so they can quickly find records, schedule care, and track priorities. It reduces duplicate entry, improves visibility of upcoming appointments, and provides a clear dashboard view of workload.

### Target Audience

- Clinic administrators who need to manage services and schedules
- Clinicians who need fast access to patient details and appointment info
- Supervisors who need at-a-glance operational metrics

## 👥 User Stories

- As a receptionist, I can create a new patient record so the patient can be booked in.
- As a clinician, I can edit a patient record to keep medical notes up to date.
- As an admin, I can add or remove services to keep the catalog current.
- As a scheduler, I can create, edit, or cancel appointments and see changes immediately.
- As a manager, I can view dashboard summaries to understand workload and priorities.

## 🎨 UX & Design

- Clean, scannable layout with clear navigation and a consistent header across pages.
- Dashboard cards surface key statistics and recent activity to reduce time-to-information.
- Forms prioritize readable labels, logical field order, and inline feedback.
- Consistent table layouts with visible action controls for CRUD operations.

## ♿ Accessibility

- Skip-link to main content for keyboard and screen reader users.
- Visible focus states for interactive elements.
- Semantic headings and labels to improve form clarity.
- High-contrast NHS-style color palette for readability.

## 🚀 Features

### Core Functionality

- ✅ **Enhanced Patient Records**: Create, view, edit, and search patient information with status tracking and priority management
- ✅ **Patient Status Management**: Track patient status (Active, Inactive, Discharged, Deceased) with priority levels and medical notes
- ✅ **Advanced Dashboard**: Real-time statistics, patient distribution charts, appointment summaries, and recent activity tracking
- ✅ **Patient Detail Views**: Comprehensive patient profiles with calculated age, appointment history, and status management
- ✅ **NHS Services**: Manage healthcare services with detailed descriptions
- ✅ **Appointment System**: Schedule, track, and manage patient appointments
- ✅ **User Management**: Django authentication with admin/staff access
- ✅ **Search & Filter**: Real-time search across patients, services, and appointments
- ✅ **Data Validation**: Comprehensive form validation and error handling
- ✅ **Modern UI/UX**: Professional NHS-compliant design with responsive layouts and interactive elements
- ✅ **Accessibility**: WCAG-compliant interface with screen reader support

### Enhanced Features (Latest Updates)

- ✅ **Patient Status Dashboard**: Real-time patient statistics with status distribution charts
- ✅ **Priority Management**: Color-coded priority levels (Low, Medium, High, Urgent)
- ✅ **Advanced Patient Profiles**: Detailed patient views with appointment history and status tracking
- ✅ **Status Management Interface**: Dedicated forms for updating patient status and priority
- ✅ **Enhanced UI Components**: Modern card layouts, badges, and responsive grid systems
- ✅ **Calculated Fields**: Automatic age calculation, appointment counting, and next appointment tracking
- ✅ **Professional Styling**: NHS-compliant color scheme with modern typography and interactive elements

### Technical Features

- ✅ **Database Migrations**: Automated schema management with Django migrations
- ✅ **Security**: CSRF protection, secure password hashing, session management
- ✅ **Testing**: Comprehensive test suite with pytest and coverage reporting
- ✅ **Production Ready**: Gunicorn WSGI server configuration
- ✅ **Environment Management**: Flexible configuration for development/testing/production
- ✅ **Data Seeding**: Automated dummy data generation for testing and demos

## 📋 Requirements

- **Python 3.8+**
- **Django 5.0+**
- **SQLite** (default) or **PostgreSQL** (production)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

## 🎆 Latest Updates & Features

### 📊 Enhanced Dashboard

- **Real-time Statistics**: Patient counts, appointment summaries, service usage metrics
- **Status Distribution**: Visual breakdown of patient statuses with color-coded badges
- **Quick Actions**: Fast navigation cards for common tasks
- **Recent Activity**: Live feed of patient registrations and appointment updates
- **Responsive Grid Layout**: Professional card-based design that works on all devices

### 👥 Advanced Patient Management

- **Comprehensive Status Tracking**: Active, Inactive, Discharged, Deceased with visual indicators
- **Priority Levels**: Low, Medium, High, Urgent with color-coded badges
- **Medical Notes**: Free-text clinical observations and notes
- **Detailed Patient Profiles**: Age calculation, appointment history, next appointment tracking
- **Dedicated Status Editor**: Streamlined interface for updating patient status and priority
- **Enhanced Forms**: Modern, accessible forms with comprehensive validation

### 🎨 Modern UI/UX Design

- **NHS-Compliant Styling**: Professional healthcare color scheme and typography
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, smooth transitions, and intuitive navigation
- **Accessibility**: WCAG-compliant with screen reader support and keyboard navigation
- **Status Badges**: Visual indicators for patient status and priority levels
- **Grid Layouts**: Modern card-based layouts with flexible responsive grids

## ⚡ Quick Start

### 1. Automated Setup (Windows)

Run the automated setup script that handles everything:

```powershell
.\setup.ps1
```

This script will:

- Create and activate a Python virtual environment
- Install all dependencies (excluding PostgreSQL packages for SQLite setup)
- Generate secure configuration with random SECRET_KEY
- Initialize and migrate the database
- Seed admin user and roles
- Optionally populate with comprehensive dummy data
- Launch the development server

### 2. Manual Setup

If you prefer manual setup or are on a different platform:

```bash
# Clone the repository
git clone <repository-url>
cd nhs_service_tracker

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env  # Edit with your configuration

# Initialize database
python manage.py migrate

# Seed initial data
python manage.py seed

# Optional: Add dummy data
python manage.py seed_data

# Run development server
python manage.py runserver
```

## 🔐 Default Login Credentials

After running the setup, use these credentials to access the system:

- **Email**: `admin@example.nhs.uk`
- **Password**: `ChangeMe123!`
- **Role**: Administrator (full system access)

> ⚠️ **Security Note**: Change the default password immediately after first login!

## 🗃️ Database Schema

### Core Models

#### Users

- Secure authentication with password hashing
- Django authentication with staff/admin access for management features
- Email-based login system

#### Patients

- NHS number (unique identifier)
- Full demographics (name, date of birth)
- Contact information (phone, email)
- Status tracking (Active, Inactive, Discharged, Deceased)
- Priority levels (Low, Medium, High, Urgent)
- Medical notes and clinical observations
- Automatic timestamps (created_at, updated_at)
- Calculated properties (age, next appointment, total appointments)
- Appointment history tracking

#### Services

- Comprehensive NHS service catalog
- Detailed descriptions
- Service-specific appointment management

#### Appointments

- Patient-service scheduling
- Date/time tracking with timezone support
- Location and status management
- Notes and follow-up tracking

## 🏗️ Project Structure

```plaintext
nhs_service_tracker/
├── nhs_service_tracker/          # Django project package
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
├── tracker/                      # Django app (views, models, forms)
│   ├── __init__.py
│   ├── views.py                 # Views and route handlers
│   ├── models.py                # Django models
│   ├── forms.py                 # Django forms
│   └── migrations/              # Django migration files
├── templates/                    # Django templates
│   ├── base.html                # Base template with navigation
│   ├── index.html               # Dashboard homepage
│   ├── auth/                    # Authentication templates
│   ├── patients/                # Patient management templates
│   ├── services/                # Service management templates
│   └── appointments/            # Appointment templates
├── static/                       # Static assets (CSS/JS)
├── tests/                       # Test suite
│   ├── conftest.py             # Test configuration
│   ├── test_auth_routes.py     # Authentication tests
│   ├── test_crud.py            # CRUD operation tests
│   └── test_models.py          # Database model tests
├── docs/                        # Documentation
├── instance/                    # Instance-specific files
├── manage.py                    # CLI commands and data seeding
├── wsgi.py                      # WSGI entry point
├── requirements.txt             # Python dependencies
├── setup.ps1                    # Automated Windows setup
├── seed-dummy-data.ps1          # Dummy data seeding script
├── verify_data.py               # Database verification utility
├── Procfile                     # Heroku deployment configuration
└── README.md                    # This file
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tracker

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Manual Testing

Manual test cases and results are documented in [TEST_PLAN.md](TEST_PLAN.md), including CRUD flows, accessibility checks, and responsive layout checks.

### Code Quality

```bash
# Lint code
flake8 tracker/ nhs_service_tracker/ tests/

# Check test coverage
coverage run -m pytest
coverage report
coverage html  # Generate HTML report
```

### Project Health & Checks

- Use the VS Code Problems panel to review linting or type errors.
- Apply Django migrations after model changes.
- Run the test suite after functional changes or before deployment.

### Database Management

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Data Management

```bash
# Seed basic admin user
python manage.py seed

# Populate with comprehensive dummy data
python manage.py seed_data

# Verify database contents
python verify_data.py
```

## 🔧 Configuration

### Environment Variables

Create an `env` file in the project root for local development (the setup script creates this for you):

```env
DJANGO_SETTINGS_MODULE=nhs_service_tracker.settings
DEBUG=1
SECRET_KEY=dev-insecure-key-change-me
DATABASE_URL=sqlite:///nhs_tracker.db
```

### Django Settings

- **Settings module**: `nhs_service_tracker.settings`
- **Environment file**: `env` (optional) is loaded for local overrides

### Database Configuration

**SQLite** (Default - Development):

```env
DATABASE_URL=sqlite:///nhs_tracker.db
```

**PostgreSQL** (Production):

```env
DATABASE_URL=postgresql://username:password@localhost/dbname
```

## 🚀 Deployment

### Heroku Deployment

The application includes a `Procfile`, a `runtime.txt`, and an `app.json` to make Heroku setup simple.

#### Quick Heroku Setup

```bash
# Login and create app
heroku login
heroku create nhs-service-tracker

# Add Postgres (sets DATABASE_URL)
heroku addons:create heroku-postgresql:essential-0 --app nhs-service-tracker

# Set required config
heroku config:set SECRET_KEY="<your-secret-key>" --app nhs-service-tracker
heroku config:set DEBUG=0 --app nhs-service-tracker

# Deploy
git push heroku main

# Run migrations and seed data
heroku run python manage.py migrate --app nhs-service-tracker
heroku run python manage.py seed --app nhs-service-tracker
heroku run python manage.py seed_data --app nhs-service-tracker

# View logs
heroku logs --tail --app nhs-service-tracker
```

#### One-click Deploy (Recommended)

1. Create the app from this repo in the Heroku Dashboard.
2. The `app.json` will auto-create a Postgres database, generate `SECRET_KEY`, and run migrations + seeding.
3. Open the app and sign in with the seeded admin user.

#### CLI Deploy

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Add Postgres (sets DATABASE_URL)
heroku addons:create heroku-postgresql:essential-0 --app your-app-name

# Set environment variables
heroku config:set DEBUG=0 --app your-app-name

# Deploy
git push heroku main

# Run migrations and seed
heroku run python manage.py migrate --app your-app-name
heroku run python manage.py seed --app your-app-name
```

### Production Deployment

For production servers:

1. Use a production WSGI server (Gunicorn included)
2. Configure PostgreSQL database
3. Set secure environment variables
4. Enable HTTPS/SSL
5. Configure proper logging
6. Set up monitoring and backups

## 🔒 Security Features

- **Password Security**: Django password hashing
- **Session Management**: Django authentication sessions
- **CSRF Protection**: Django CSRF middleware
- **Login Protection**: Django `login_required` decorators on protected views
- **Input Validation**: Comprehensive form validation
- **SQL Injection Prevention**: Django ORM parameterized queries
- **Environment Isolation**: Separate configs for dev/test/prod
- **Secret Key Management**: `SECRET_KEY` stored in environment variables for production

## 🎯 Authentication & Access

- The app uses Django authentication for sign-in and protects CRUD routes with `login_required`.
- Administrative tasks (like Django admin access) are handled through Django's built-in staff/superuser flags.

## 📊 Dummy Data

The application includes comprehensive dummy data for testing:

### NHS Services (12 total)

- General Practice
- Cardiology
- Dermatology
- Orthopedics
- Mental Health
- Physiotherapy
- Radiology
- Blood Tests
- Vaccination
- Diabetes Care
- Respiratory Care
- Ophthalmology

### Sample Patients (15 realistic records)

- Complete demographics with NHS numbers
- Varied ages and contact information
- Realistic names and data
- Status distribution: Active, Inactive, Discharged, Deceased
- Priority levels: Low, Medium, High, Urgent
- Medical notes and clinical observations

### Appointments (200+ records)

- 90-day span (30 days past, 60 days future)
- Realistic scheduling (9 AM - 5 PM)
- Various statuses and locations
- Meaningful notes and follow-ups

## 🧪 Testing

### Test Coverage

- **Authentication**: Login and registration flows
- **CRUD Operations**: Create, read, update, and delete for core entities
- **Database Models**: Relationships and calculated fields
- **Security**: Authentication checks and form validation
- **Manual Testing**: Documented in [TEST_PLAN.md](TEST_PLAN.md)

### Running Specific Tests

```bash
# Authentication tests
pytest tests/test_auth_routes.py

# Model tests
pytest tests/test_models.py

# CRUD tests
pytest tests/test_crud.py
```

## 📚 API Documentation

The application follows RESTful URL patterns:

### Patient Management

- `GET /patients/` - List patients (with search)
- `GET /patients/create` - Create patient form
- `POST /patients/create` - Submit new patient
- `GET /patients/<id>` - View patient details
- `GET /patients/<id>/edit` - Edit patient form
- `POST /patients/<id>/edit` - Update patient
- `GET /patients/<id>/status` - Edit patient status form
- `POST /patients/<id>/status` - Update patient status and priority
- `POST /patients/<id>/delete` - Delete patient

### Service Management

- `GET /services/` - List services
- `GET /services/create` - Create service form
- `POST /services/create` - Submit new service
- `GET /services/<id>/edit` - Edit service form
- `POST /services/<id>/edit` - Update service
- `POST /services/<id>/delete` - Delete service

### Appointment Management

- `GET /appointments/` - List appointments (with search)
- `GET /appointments/create` - Create appointment form
- `POST /appointments/create` - Submit new appointment
- `GET /appointments/<id>/edit` - Edit appointment form
- `POST /appointments/<id>/edit` - Update appointment
- `POST /appointments/<id>/delete` - Delete appointment

## 🛠️ Troubleshooting

### Common Issues

**Database Issues**:

```bash
# Reset database
rm instance/*.db
python manage.py migrate
python manage.py seed
```

**Permission Errors**:

- Ensure virtual environment is activated
- Check file permissions in instance/ directory
- Verify Python path in virtual environment

**Import Errors**:

- Reinstall requirements: `pip install -r requirements.txt`
- Check Python version compatibility
- Verify virtual environment activation

**Port Already in Use**:

```bash
# Use different port
python manage.py runserver 5001
```

### Development Tips

1. **Database Debugging**: Use `sqlite3` CLI or DB Browser for SQLite
2. **Log Debugging**: Check Django debug output in development mode
3. **Form Debugging**: Use browser developer tools to inspect form data
4. **Template Debugging**: Enable Django template debug mode for better error messages
5. **Patient Status Testing**: Use the dedicated status management interface to test priority and status updates
6. **Dashboard Testing**: Check real-time statistics by adding/editing patients and appointments
7. **UI Testing**: Test responsive design across different screen sizes and devices

## 👤 User Guide

### Getting Started

1. Sign in with your administrator account.
2. Review the dashboard for key totals and upcoming activity.
3. Use the navigation bar to access Patients, Services, and Appointments.

### Managing Patients

- Add patients from Patients → Add Patient.
- Use search to find patients by name or NHS number.
- Open a patient record to view details and appointment history.
- Update status/priority to reflect current care needs.

### Managing Services

- Add or update services from Services → Add Service.
- Keep descriptions clear so clinicians can pick the right service.

### Managing Appointments

- Schedule appointments from Appointments → Schedule Appointment.
- Review upcoming appointments on the dashboard.
- Update or cancel appointments as needed.

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make changes and add tests
4. Run the test suite (`pytest`)
5. Commit changes (`git commit -am 'Add new feature'`)
6. Push to branch (`git push origin feature/new-feature`)
7. Create a Pull Request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🤝 Support

For support, please create an issue on the GitHub repository or contact the development team.

## 🏗️ Future Enhancements

- ✅ **Enhanced Dashboard**: Real-time statistics and patient status analytics (COMPLETED)
- ✅ **Patient Status Management**: Comprehensive status tracking with priority levels (COMPLETED)
- ✅ **Modern UI/UX**: Professional NHS-compliant responsive design (COMPLETED)
- [ ] **Calendar Integration**: Full calendar view for appointments
- [ ] **Email Notifications**: Appointment reminders and confirmations
- [ ] **Mobile App**: Native iOS/Android applications
- [ ] **API Endpoints**: RESTful API for third-party integrations
- [ ] **Document Management**: Patient file uploads and management
- [ ] **Audit Trail**: Complete action logging and history tracking
- [ ] **Multi-language Support**: Internationalization for diverse communities
- [ ] **Advanced Reporting**: Detailed analytics with export capabilities
- [ ] **Integration APIs**: Third-party system integrations (NHS Spine, PAS systems)

---

## 🏥 Built for Healthcare Professionals

Built with ❤️ for the NHS and healthcare professionals worldwide. This application demonstrates modern web development practices applied to healthcare management, providing a robust, secure, and user-friendly platform for patient care coordination.
