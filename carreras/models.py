from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

class Carrera(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Nombre de la Carrera")
    slug = models.SlugField(max_length=200, unique=True)
    resumen = models.CharField(max_length=300)
    
    contenido_completo = CKEditor5Field(config_name='default', verbose_name="Información Detallada")
    
    duracion = models.CharField(max_length=50, verbose_name="Duración")
    imagen_portada = models.ImageField(upload_to='carreras/', null=True, blank=True) 

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('carreras:detalle_carrera', kwargs={'slug': self.slug})


class ImagenCarrera(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='imagenes', verbose_name="Carrera")
    imagen = models.ImageField(upload_to='carreras/galeria/', verbose_name="Imagen adicional")
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Descripción corta (Opcional)")

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Galería de Imágenes"

    def __str__(self):
        return f"Foto para {self.carrera.titulo}"