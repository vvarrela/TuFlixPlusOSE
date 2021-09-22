from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaPrueba(request):
    return HttpResponse("Bienvenido a Usuario")