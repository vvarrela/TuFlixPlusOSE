from django.urls import path
from Servicios.views import Ejemplo

urlpatterns = [
    path('ejemplo',Ejemplo)
]
