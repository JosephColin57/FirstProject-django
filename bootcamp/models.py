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


# La foreing key se pone en la N en las relaciones 1 - N
# 1 generation - N koders
# N mentors - N Generations
# Cuando hay N - N la FK se pone en el mas chico jerarquicamente --> Mentors
# 1 bootcamp - N Generations


class Bootcamp(models.Model):
    """Bootcamp model"""

    name = models.CharField(
        max_length=255, unique=True, null=False, default="Nombre por defecto"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bootcamp: {self.name}"


class Generation(models.Model):
    """Generation Model."""

    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")

    def __str__(self):
        return f"Generation: {self.number} {self.bootcamp.name}"


class Koder(models.Model):
    """Koder Model."""

    STATUSES = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("finished", "Finalizado"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=10, choices=STATUSES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreing Keys
    # Related name buena practica --> Nombre del modelo en plural
    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")

    # Representación en string de un objeto
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"


class Mentor(models.Model):
    """Mentor Model."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
        return f"id: {self.pk} {self.first_name} {self.last_name}"


# Koders pertenece a 1 generacion -> 1 generation - N koders
# Mentores pertenece a varias generaciones -> N mentors - N Generations
# Generaciones pertenecen a un bootcamp -> 1 bootcamp - N Generations
