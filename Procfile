release: python manage.py migrate --noinput && python manage.py seed
web: gunicorn nhs_service_tracker.wsgi:application
