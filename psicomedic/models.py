from django.db import models


# Create your models here.
class Psychologist(models.Model):
    """Psychologist model"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Psychologist: {self.first_name} {self.last_name}"


class Patient(models.Model):
    """Patient model"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    biography = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"Patient: {self.first_name} {self.last_name}"


class Appointment(models.Model):
    """Appointment model"""

    title = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, models.PROTECT, related_name="appointments")
    psychologist = models.ForeignKey(
        Psychologist, models.PROTECT, related_name="appointments"
    )

    def __str__(self):
        return f"Appointment: {self.title} {self.appointment_date}"
