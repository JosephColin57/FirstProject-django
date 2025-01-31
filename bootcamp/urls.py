from django.contrib import admin
from django.urls import path

# Importar la vista creada
from .views import list_koders, get_koder

urlpatterns = [
    path('koders/', list_koders), # Agregar la vista creada
    path('koders/<int:id>/', get_koder), # Agregar la vista creada
 ]