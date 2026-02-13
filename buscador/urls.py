from django.urls import path
from . import views

app_name = "buscador"
urlpatterns = [
    # Ej. /buscador/
    path("", views.VistaInicioBuscador.as_view(), name="inicio_buscador"),

    # Ej. /buscador/5/
    path("<int:pk>/", views.VistaDetalles.as_view(), name="detalles"),
]