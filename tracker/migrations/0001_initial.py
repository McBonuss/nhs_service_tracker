# Generated manually for initial schema
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nhs_number", models.CharField(max_length=12, unique=True)),
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("date_of_birth", models.DateField()),
                ("contact_phone", models.CharField(blank=True, max_length=30)),
                ("contact_email", models.EmailField(blank=True, max_length=254)),
                ("status", models.CharField(choices=[("active", "Active"), ("inactive", "Inactive"), ("discharged", "Discharged"), ("deceased", "Deceased")], default="active", max_length=20)),
                ("priority", models.CharField(choices=[("low", "Low"), ("medium", "Medium"), ("high", "High"), ("urgent", "Urgent")], default="medium", max_length=20)),
                ("medical_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("scheduled_for", models.DateTimeField()),
                ("location", models.CharField(max_length=120)),
                ("status", models.CharField(choices=[("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled"), ("no-show", "No Show")], default="scheduled", max_length=20)),
                ("notes", models.TextField(blank=True)),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="appointments", to="tracker.patient")),
                ("service", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tracker.service")),
            ],
        ),
    ]
