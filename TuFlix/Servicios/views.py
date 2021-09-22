from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Ejemplo(request):
    return HttpResponse("Bienvenido a Servicios")