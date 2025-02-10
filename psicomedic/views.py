from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import Psychologist, Patient, Appointment

def list_psychologists(request):
    psychologists = Psychologist.objects.all()
    print(f"Psychologists -> {psychologists}")

    template = loader.get_template("templates/list_psychologists.html")

    context= {"psychologists": psychologists}

    return HttpResponse(template.render(context, request))

def get_psychologist(request, id):
    psychologists = Psychologist.objects.all()

    for p in psychologists:
        if p.id == id:
            psychologist = p
            break

    template = loader.get_template("templates/get_psychologist.html")

    context = {"psychologist": psychologist}

    print(f"Found Psychologist -> {psychologist}")
    return HttpResponse(template.render(context, request))

def list_patients(request):
    patients = Patient.objects.all()
    print(f"Patients -> {patients}")

    template= loader.get_template("templates/list_patients.html")

    context={"patients": patients}

    return HttpResponse(template.render(context, request))

def get_patient(request, id):
    patients = Patient.objects.all()

    for p in patients:
        if p.id == id:
            patient = p
            break

    template = loader.get_template("templates/get_patient.html")

    context = {"patient": patient}

    print(f"Found Patient -> {patient}")
    return HttpResponse(template.render(context, request))

def list_appointments(request):
    appointments = Appointment.objects.all()
    print(f"Appointments -> {appointments}")

    template = loader.get_template("templates/list_appointments.html")

    context = {"appointments": appointments}

    return HttpResponse(template.render(context, request))

def get_appointment(request, id):
    appointments = Appointment.objects.all()

    for a in appointments:
        if a.id == id:
            appointment = a
            break

    template = loader.get_template("templates/get_appointment.html")

    context = {"appointment": appointment}

    print(f"Found Appointment -> {appointment}")
    return HttpResponse(template.render(context, request))