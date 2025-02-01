from django.shortcuts import render

# importar HTTPResponse
from django.http import HttpResponse

from django.template import loader

# Create your views here.

# Las vistas son funciones que reciben una petición web y devuelven una respuesta web.


def bienvenida(request):
    return HttpResponse("Hola, bienvenido a mi aplicación web.")


def saludo(request):
    return HttpResponse("Hola, ¿cómo estás?")


def saludoConNombre(request, nombre):
    context = {
        # "name": nombre,
        "apellido": "Colin",
    }  # Va a servir para enviar información al template
    template = loader.get_template(
        "base.html"
    )  # o tambien se puede poner la ruta "myApp/base.html" o la ruta de la app
    return HttpResponse(template.render(context, request))


def saludoCondicionado(request, type):
    if type == "mentor":
        return HttpResponse("Hello mentor here are your classes")
    elif type == "koder":
        return HttpResponse("Hello koder welcome to kodemia")
    else:
        return HttpResponse("You are not welcome here")


def practica2(request, name, type):
    context = {"name": name, "type": type}
    template = loader.get_template("practica2.html")
    return HttpResponse(template.render(context, request))
