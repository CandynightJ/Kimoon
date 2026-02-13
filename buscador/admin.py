from django.contrib import admin

from .models import Actividad, Area

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "modalidad")
    search_fields = ("nombre",)
    filter_horizontal = ("area",)  # ManyToMany normal

admin.site.register(Area)