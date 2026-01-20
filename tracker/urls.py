from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("patients/", views.patients_list, name="patients_list"),
    path("patients/add/", views.patients_create, name="patients_create"),
    path("patients/<int:pk>/", views.patients_detail, name="patients_detail"),
    path("patients/<int:pk>/edit/", views.patients_edit, name="patients_edit"),

    path("services/", views.services_list, name="services_list"),
    path("services/add/", views.services_create, name="services_create"),

    path("appointments/", views.appointments_list, name="appointments_list"),
    path("appointments/add/", views.appointments_create, name="appointments_create"),
]
