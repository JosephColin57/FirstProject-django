from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def list_koders(request):
    # creamos contexto 
    context = { 
        "bootcamp" : {
            "name": "Python Bootcamp",
            "language": "Python",
            "duration": "3 months"
        },
    "koders" : [
        {"name": "David", "age": 22, "email": "david@test.com"},
        {"name": "Jorge", "age": 25, "email": "jorge@test.com"},
        {"name": "Rosa", "age": 23, "email": "rosa@test.com"},
    ] 
    }
    #creamos templates
    template = loader.get_template("templates/list_koders.html")
    return HttpResponse(template.render(context, request))


def get_koder(request, id):

    koders = [
        {"id": 1, "name": "David", "age": 22, "email": "david@test.com"},
        {"id": 2, "name": "Jorge", "age": 25, "email": "jorge@test.com"},
        {"id": 3, "name": "Rosa", "age": 23, "email": "rosa@test.com"},
    ]

    koder = [koder for koder in koders if koder["id"] == id]

    if not koder:
        return HttpResponse("Koder not found")

    print(f"Found Koder -> {koder}")
    return HttpResponse(f"Found Koder -> {koder}")
