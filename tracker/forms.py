from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Service, Appointment


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    full_name = forms.CharField(label="Full name", max_length=120)

    class Meta:
        model = User
        fields = ("email", "full_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"].lower()
        user.email = self.cleaned_data["email"].lower()
        user.first_name = self.cleaned_data["full_name"]
        if commit:
            user.save()
        return user


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "nhs_number",
            "first_name",
            "last_name",
            "date_of_birth",
            "contact_phone",
            "contact_email",
            "status",
            "priority",
            "medical_notes",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "patient",
            "service",
            "scheduled_for",
            "location",
            "status",
            "notes",
        ]
        widgets = {
            "scheduled_for": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
