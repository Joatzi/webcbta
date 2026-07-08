
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class ActividadAlumno(models.Model):
    titulo = models.CharField(max_length=250, verbose_name="Título de la Actividad/Aviso")
    contenido = CKEditor5Field(config_name='default', verbose_name="Detalle de la Actividad")
    imagen_destacada = models.ImageField(upload_to='alumnos/%Y/%m/%d/', blank=True, null=True, verbose_name="Imagen Opcional")
    fecha_publicacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Publicación")

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = "Actividad de Alumno"
        verbose_name_plural = "Actividades de Alumnos"

    def __str__(self):
        return self.titulo