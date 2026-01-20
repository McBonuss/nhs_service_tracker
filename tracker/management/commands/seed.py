from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seed a default admin user."

    def handle(self, *args, **options):
        email = "admin@example.nhs.uk"
        password = "ChangeMe123!"
        if not User.objects.filter(username=email).exists():
            user = User.objects.create_superuser(
                username=email,
                email=email,
                password=password,
                first_name="Admin",
                last_name="User",
            )
            self.stdout.write(self.style.SUCCESS(f"Created admin user: {email} / {password}"))
        else:
            self.stdout.write(self.style.WARNING("Admin user already exists."))
