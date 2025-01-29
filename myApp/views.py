from django.shortcuts import render

# importar HTTPResponse
from django.http import HttpResponse

# Create your views here.

# Las vistas son funciones que reciben una petición web y devuelven una respuesta web.

def bienvenida(request):
    return HttpResponse("Hola, bienvenido a mi aplicación web.")

def saludo(request):
    return HttpResponse("Hola, ¿cómo estás?")