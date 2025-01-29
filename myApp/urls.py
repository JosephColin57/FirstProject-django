from django.contrib import admin
from django.urls import path

# Importar la vista creada
from .views import bienvenida, saludo, saludoConNombre

urlpatterns = [
    path('', bienvenida), # Agregar la vista creada
    path('saludo/', saludo), # Agregar la vista creada
    path('saludo/<str:nombre>/', saludoConNombre), # Agregar la vista creada
]
