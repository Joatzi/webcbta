from django.shortcuts import render, get_object_or_404
from .models import Carrera


def lista_carreras(request):
    carreras = Carrera.objects.all().order_by('titulo')
    return render(request, 'carreras/lista.html', {'carreras': carreras})

def detalle_carrera(request, slug):
    carrera = get_object_or_404(Carrera, slug=slug)
    return render(request, 'carreras/detalle.html', {'carrera': carrera})