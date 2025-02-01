from django.contrib import admin
from django.urls import path

# Importar la vista creada
from .views import bienvenida, saludo, saludoConNombre, saludoCondicionado, practica2

urlpatterns = [
    path('', bienvenida), # Agregar la vista creada
    path('saludo/', saludo), # Agregar la vista creada
    path('saludo/<str:nombre>/', saludoConNombre), # Agregar la vista creada
    path('kodemia/<str:type>/', saludoCondicionado), # Agregar la vista creada

    path('kodemia/<str:name>/<str:type>/', practica2), # Agregar la vista creada
]
