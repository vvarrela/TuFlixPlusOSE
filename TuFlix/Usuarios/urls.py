from Servicios.views import Ejemplo
from django.urls import path
from Usuarios.views import Ejemplo

urlpatterns = [
    path('ejemplo',Ejemplo)
]
