from django.db import models
from django_countries.fields import CountryField
from django_countries import countries

GENEROS = [
    ("F", "Femenino"),
    ("M", "Masculino"),
    ("T", "Todos"),
]

GRADOS = [
    ("PK", "Pre Kinder"),
    ("K", "Kinder"),
    ("1B", "1° Básico"),
    ("2B", "2° Básico"),
    ("3B", "3° Básico"),
    ("4B", "4° Básico"),
    ("5B", "5° Básico"),
    ("6B", "6° Básico"),
    ("7B", "7° Básico"),
    ("8B", "8° Básico"),
    ("1M", "1° Medio"),
    ("2M", "2° Medio"),
    ("3M", "3° Medio"),
    ("4M", "4° Medio"),
    ("Uni", "Universitario"),
]

MODALIDAD = [
    ("P", "Presencial"),
    ("O", "Online"),
    ("H", "Híbrido"),
]

TIPO = [
    ("TV", "Taller de verano"),
    ("TI", "Taller de invierno"),
    ("O", "Olimpiada"),
    ("CON", "Concurso"),
    ("COM", "Competencia"),
    ("CU", "Curso"),
]

class Actividad(models.Model):
    # Descripción general
    nombre = models.CharField(max_length=255)
    descripcion_breve = models.TextField()
    descripcion_larga = models.TextField()

    # Detalles
    modalidad = models.CharField(max_length=3, choices=MODALIDAD, blank=True)
    link = models.URLField(blank=True, null=True)
    organizador = models.CharField(max_length=255, blank=True)
    costo = models.IntegerField(blank=True, null=True)
    area = models.ManyToManyField("buscador.Area")
    duracion = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=3, choices=TIPO)
    genero = models.CharField(max_length=3, choices=GENEROS, blank=True)

    # Edad
    edad_min = models.IntegerField(blank=True, null=True)
    edad_max = models.IntegerField(blank=True, null=True)
    grado_min = models.CharField(max_length=3, choices=GRADOS, blank=True)
    grado_max = models.CharField(max_length=3, choices=GRADOS, blank=True)
    
    # Lugar
    pais = CountryField(multiple=True, blank=True)
    lugar = models.CharField(max_length=255, blank=True)

    # Fechas
    inicio_postulacion = models.DateField(blank=True, null=True)
    cierre_postulacion = models.DateField(blank=True, null=True)
    inicio_actividad = models.DateField(blank=True, null=True)
    termino_actividad = models.DateField(blank=True, null=True)

    # Más Información
    otros_requisitos = models.TextField(blank=True)
    info_extra = models.TextField(blank=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.nombre
    
    def nombres_paises(self):
        return [countries.name(code) for code in self.pais]
    

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Área'"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.nombre

