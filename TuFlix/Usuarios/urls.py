from django.urls import path
from Usuarios.views import vistaPrueba

urlpatterns = [
    path('prueba', vistaPrueba)
]
