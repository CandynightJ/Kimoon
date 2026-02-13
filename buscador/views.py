from django.shortcuts import render
from django.views import generic

from .models import Actividad

class VistaInicioBuscador(generic.ListView):
    template_name = "buscador/inicio.html"
    model = Actividad
    context_object_name = "lista_actividades"

class VistaDetalles(generic.DetailView):
    model = Actividad
    template_name = "buscador/detalles.html"