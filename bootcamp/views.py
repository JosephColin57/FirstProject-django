from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def list_koders(request):
    koders = [
        {"name": "David", "age": 22, "email": "david@test.com"},
        {"name": "Jorge", "age": 25, "email": "jorge@test.com"},
        {"name": "Rosa", "age": 23, "email": "rosa@test.com"},
    ]
    return HttpResponse(koders)


def get_koder(request, id):
    koders = [
        {"id": 1, "name": "David", "age": 22, "email": "david@test.com"},
        {"id": 2, "name": "Jorge", "age": 25, "email": "jorge@test.com"},
        {"id": 3, "name": "Rosa", "age": 23, "email": "rosa@test.com"},
    ]
    koder = [koder for koder in koders if koder["id"] == id]
    return HttpResponse(koder)
