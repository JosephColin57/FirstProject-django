from django.shortcuts import render

# importar HTTPResponse
from django.http import HttpResponse

# Create your views here.

# Las vistas son funciones que reciben una petición web y devuelven una respuesta web.

def bienvenida(request):
    return HttpResponse("Hola, bienvenido a mi aplicación web.")

def saludo(request):
    return HttpResponse("Hola, ¿cómo estás?")

def saludoConNombre(request, nombre):
    print("imprimiendo nombre: ", nombre)
    return HttpResponse(f"Hola, {nombre}. Mucho gusto en saludarte.")

def saludoCondicionado(request, type):
    if type == "mentor":
        return HttpResponse("Hello mentor here are your classes")
    elif type == "koder":
        return HttpResponse("Hello koder welcome to kodemia")
    else:
        return HttpResponse("You are not welcome here")