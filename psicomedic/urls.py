from django.contrib import admin
from django.urls import path

# Importar la vista creada

from .views import list_psychologists, get_psychologist, list_patients, get_patient, list_appointments, get_appointment

urlpatterns = [
    path("psychologists/", list_psychologists),
    path("psychologists/<int:id>/", get_psychologist),
    path("patients/", list_patients),
    path("patient/<int:id>/", get_patient),
    path("appointments/", list_appointments),
    path("appointment/<int:id>/", get_appointment),
]
