# NHS Service Tracker

A comprehensive Flask web application for managing NHS patients, services, and appointments. Built with modern web technologies and designed for healthcare professionals to efficiently track and manage patient care workflows.

## 🏥 Overview

The NHS Service Tracker is a full-featured healthcare management system that provides:

- **Patient Management**: Complete patient records with NHS numbers, demographics, and contact information
- **Service Management**: Comprehensive NHS service catalog (Cardiology, Mental Health, GP services, etc.)
- **Appointment Scheduling**: Advanced booking system with status tracking and location management
- **User Authentication**: Secure role-based access control with admin and clinician roles
- **Search & Filtering**: Powerful search functionality across all entities
- **Responsive Design**: Mobile-friendly interface following NHS design principles

## 🚀 Features

### Core Functionality

- ✅ **Patient Records**: Create, view, edit, and search patient information
- ✅ **NHS Services**: Manage healthcare services with detailed descriptions
- ✅ **Appointment System**: Schedule, track, and manage patient appointments
- ✅ **User Management**: Role-based authentication (Admin/Clinician)
- ✅ **Search & Filter**: Real-time search across patients, services, and appointments
- ✅ **Data Validation**: Comprehensive form validation and error handling
- ✅ **Accessibility**: WCAG-compliant interface with screen reader support

### Technical Features

- ✅ **Database Migrations**: Automated schema management with Alembic
- ✅ **Security**: CSRF protection, secure password hashing, session management
- ✅ **Testing**: Comprehensive test suite with pytest and coverage reporting
- ✅ **Production Ready**: Gunicorn WSGI server configuration
- ✅ **Environment Management**: Flexible configuration for development/testing/production
- ✅ **Data Seeding**: Automated dummy data generation for testing and demos

## 📋 Requirements

- **Python 3.8+**
- **Flask 3.0+**
- **SQLite** (default) or **PostgreSQL** (production)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

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
flask --app wsgi db upgrade

# Seed initial data
flask --app manage seed

# Optional: Add dummy data
flask --app manage seed-data

# Run development server
flask --app wsgi run
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
- Role-based access control (Admin/Clinician)
- Email-based login system

#### Patients

- NHS number (unique identifier)
- Full demographics (name, date of birth)
- Contact information (phone, email)
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

```
nhs_service_tracker/
├── app/                          # Main application package
│   ├── __init__.py              # Flask application factory
│   ├── config.py                # Configuration management
│   ├── extensions.py            # Flask extensions setup
│   ├── forms.py                 # WTForms form classes
│   ├── models.py                # SQLAlchemy database models
│   ├── security.py              # Role-based access decorators
│   ├── static/                  # Static assets
│   │   ├── css/styles.css       # NHS-compliant styling
│   │   └── js/app.js           # Frontend JavaScript
│   ├── templates/               # Jinja2 templates
│   │   ├── base.html           # Base template with navigation
│   │   ├── index.html          # Dashboard homepage
│   │   ├── auth/               # Authentication templates
│   │   ├── patients/           # Patient management templates
│   │   ├── services/           # Service management templates
│   │   └── appointments/       # Appointment templates
│   └── views/                   # Flask blueprints/routes
│       ├── __init__.py
│       ├── auth.py             # Authentication routes
│       ├── main.py             # Dashboard routes
│       ├── patients.py         # Patient management
│       ├── services.py         # Service management
│       └── appointments.py     # Appointment scheduling
├── migrations/                  # Database migration files
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
pytest --cov=app

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Lint code
flake8 app/

# Check test coverage
coverage run -m pytest
coverage report
coverage html  # Generate HTML report
```

### Database Management

```bash
# Create new migration
flask --app wsgi db migrate -m "Description of changes"

# Apply migrations
flask --app wsgi db upgrade

# Downgrade migration
flask --app wsgi db downgrade

# Reset database (development only)
flask --app wsgi db downgrade base
flask --app wsgi db upgrade
```

### Data Management

```bash
# Seed basic roles and admin user
flask --app manage seed

# Populate with comprehensive dummy data
flask --app manage seed-data

# Verify database contents
python verify_data.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
FLASK_APP=wsgi.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///nhs_tracker.db
```

### Configuration Classes

- **DevelopmentConfig**: Debug enabled, SQLite database
- **TestingConfig**: In-memory SQLite, CSRF disabled for testing
- **ProductionConfig**: Debug disabled, PostgreSQL recommended

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

The application includes a `Procfile` for Heroku deployment:

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set DATABASE_URL=your-database-url

# Deploy
git push heroku main

# Run migrations
heroku run flask --app wsgi db upgrade

# Seed initial data
heroku run flask --app manage seed
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

- **Password Security**: Werkzeug password hashing
- **Session Management**: Secure Flask-Login sessions
- **CSRF Protection**: Flask-WTF CSRF tokens
- **Role-Based Access**: Custom decorators for authorization
- **Input Validation**: Comprehensive form validation
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **Environment Isolation**: Separate configs for dev/test/prod

## 🎯 User Roles

### Administrator

- Full system access
- User management
- Service management
- Patient and appointment management
- System configuration

### Clinician

- Patient management (create, edit, view)
- Appointment scheduling and management
- Service viewing
- Limited administrative functions

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

### Appointments (200+ records)

- 90-day span (30 days past, 60 days future)
- Realistic scheduling (9 AM - 5 PM)
- Various statuses and locations
- Meaningful notes and follow-ups

## 🧪 Testing

### Test Coverage

- **Authentication**: Login, registration, logout flows
- **CRUD Operations**: Create, read, update, delete for all entities
- **Database Models**: Relationships, constraints, validations
- **Security**: Role-based access, form validation
- **Integration**: End-to-end user workflows

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
- `GET /patients/<id>/edit` - Edit patient form
- `POST /patients/<id>/edit` - Update patient
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
flask --app wsgi db upgrade
flask --app manage seed
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
flask --app wsgi run --port 5001
```

### Development Tips

1. **Database Debugging**: Use `sqlite3` CLI or DB Browser for SQLite
2. **Log Debugging**: Check Flask debug output in development mode
3. **Form Debugging**: Use browser developer tools to inspect form data
4. **Template Debugging**: Enable Jinja2 debug mode for better error messages

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

- [ ] **Calendar Integration**: Full calendar view for appointments
- [ ] **Reporting Dashboard**: Analytics and metrics
- [ ] **Email Notifications**: Appointment reminders and confirmations
- [ ] **Mobile App**: Native iOS/Android applications
- [ ] **API Endpoints**: RESTful API for third-party integrations
- [ ] **Document Management**: Patient file uploads and management
- [ ] **Audit Trail**: Complete action logging and history tracking
- [ ] **Multi-language Support**: Internationalization for diverse communities

---

**Built with ❤️ for the NHS and healthcare professionals**
