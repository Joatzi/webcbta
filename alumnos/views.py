from django.shortcuts import render
from .models import ActividadAlumno

def modulo_alumnos(request):

    publicaciones = ActividadAlumno.objects.all()
    return render(request, 'alumnos/alumnos.html', {'publicaciones': publicaciones})