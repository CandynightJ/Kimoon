from django.shortcuts import render
from django.views import generic

from .models import Actividad

class VistaInicioBuscador(generic.ListView):
    template_name = "buscador/inicio.html"
    model = Actividad
    context_object_name = "lista_actividades"

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get("q")
        modalidad = self.request.GET.get("modalidad")
        generos = self.request.GET.getlist("genero")
        costo = self.request.GET.get("costo")

        if q:
            queryset = queryset.filter(nombre__icontains=q)

        if modalidad:
            queryset = queryset.filter(modalidad=modalidad)

        if generos:
            queryset = queryset.filter(genero__in=generos)

        if costo == "gratis":
            queryset = queryset.filter(costo=0)

        elif costo == "pagado":
            queryset = queryset.filter(costo__gt=0)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["generos_seleccionados"] = self.request.GET.getlist("genero")
        context["costo_seleccionado"] = self.request.GET.get("costo")
        return context
    

class VistaDetalles(generic.DetailView):
    model = Actividad
    template_name = "buscador/detalles.html"