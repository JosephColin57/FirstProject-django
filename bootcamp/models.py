from django.db import models

# Create your models here.

# id -> Serial (autoincremental)
# first_name -> string
# last_name -> string
# generation -> string
# email -> string
# phone -> string
# status -> (activo, dado de baja)
# address -> string
# size -> (S, M, L, XL)
# created_at -> datetime
# updated_at -> datetime
# birthday -> date

# las clases(modelos) siempre van capitalizadas -> Koder
# los modelos heredan del modelo predeterminado de django -> models.Model
# cada modelo representa una tabla en SQL
# Cada propiedad del modelo(clase) representa una atributo en la tabla


class Koder(models.Model):
    """Koder Model."""

    STATUSES = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("finished", "Finalizado"),
    ]

    SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    generation = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=10, choices=STATUSES, default="active")
    address = models.CharField(max_length=255)
    size = models.CharField(max_length=2, choices=SIZES, default="M")
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    # Representación en string de un objeto
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"
