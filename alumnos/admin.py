from django.contrib import admin
from .models import ActividadAlumno

@admin.register(ActividadAlumno)
class ActividadAlumnoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    search_fields = ('titulo', 'contenido')