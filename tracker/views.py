from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from datetime import timedelta

from .forms import AppointmentForm, LoginForm, PatientForm, RegisterForm, ServiceForm
from .models import Appointment, Patient, Service


@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    active_patients = Patient.objects.filter(status="active").count()
    high_priority_patients = Patient.objects.filter(priority="high").count()
    urgent_patients = Patient.objects.filter(priority="urgent").count()
    total_services = Service.objects.count()

    today = timezone.now().date()
    this_week = today + timedelta(days=7)

    today_appointments = Appointment.objects.filter(
        scheduled_for__date=today, status="scheduled"
    ).count()

    this_week_appointments = Appointment.objects.filter(
        scheduled_for__date__gte=today,
        scheduled_for__date__lte=this_week,
        status="scheduled",
    ).count()

    total_appointments = Appointment.objects.count()

    week_ago = timezone.now() - timedelta(days=7)
    recent_patients = (
        Patient.objects.filter(created_at__gte=week_ago)
        .order_by("-created_at")
        .all()[:5]
    )

    tomorrow_end = timezone.now() + timedelta(days=1)
    urgent_appointments = (
        Appointment.objects.filter(
            scheduled_for__gte=timezone.now(),
            scheduled_for__lte=tomorrow_end,
            status="scheduled",
        )
        .select_related("patient", "service")
        .order_by("scheduled_for")
        .all()[:5]
    )

    status_stats = dict(
        Patient.objects.values("status").annotate(count=Count("id")).values_list(
            "status", "count"
        )
    )
    priority_stats = dict(
        Patient.objects.values("priority").annotate(count=Count("id")).values_list(
            "priority", "count"
        )
    )

    return render(
        request,
        "index.html",
        {
            "total_patients": total_patients,
            "active_patients": active_patients,
            "high_priority_patients": high_priority_patients,
            "urgent_patients": urgent_patients,
            "total_services": total_services,
            "today_appointments": today_appointments,
            "this_week_appointments": this_week_appointments,
            "total_appointments": total_appointments,
            "recent_patients": recent_patients,
            "urgent_appointments": urgent_appointments,
            "status_stats": status_stats,
            "priority_stats": priority_stats,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username").lower()
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Signed in successfully.")
            return redirect("dashboard")
        messages.error(request, "Invalid credentials.")
    return render(request, "auth/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        if User.objects.filter(username=form.cleaned_data["email"].lower()).exists():
            messages.warning(request, "Email already registered.")
        else:
            user = form.save()
            login(request, user)
            messages.success(request, "Account created.")
            return redirect("dashboard")
    return render(request, "auth/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Signed out.")
    return redirect("login")


@login_required
def patients_list(request):
    query = request.GET.get("q", "")
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(nhs_number__icontains=query)
        )
    return render(request, "patients/list.html", {"patients": patients, "query": query})


@login_required
def patients_create(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient created.")
        return redirect("patients_list")
    return render(request, "patients/form.html", {"form": form, "title": "Add Patient"})


@login_required
def patients_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, "patients/detail.html", {"patient": patient})


@login_required
def patients_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient updated.")
        return redirect("patients_detail", pk=patient.pk)
    return render(request, "patients/form.html", {"form": form, "title": "Edit Patient"})


@login_required
def services_list(request):
    services = Service.objects.all()
    return render(request, "services/list.html", {"services": services})


@login_required
def services_create(request):
    form = ServiceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Service created.")
        return redirect("services_list")
    return render(request, "services/form.html", {"form": form, "title": "Add Service"})


@login_required
def appointments_list(request):
    appointments = Appointment.objects.select_related("patient", "service").order_by("-scheduled_for")
    return render(request, "appointments/list.html", {"appointments": appointments})


@login_required
def appointments_create(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Appointment created.")
        return redirect("appointments_list")
    return render(request, "appointments/form.html", {"form": form, "title": "Schedule Appointment"})
