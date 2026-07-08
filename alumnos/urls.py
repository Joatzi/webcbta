from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Espacio de nombres para que coincida con {% url 'alumnos:modulo_alumnos' %}
app_name = 'alumnos'

urlpatterns = [
    # Ruta principal para el feed híbrido de alumnos
    path('', views.modulo_alumnos, name='modulo_alumnos'),
]

# 🌟 ESTO ASEGURA QUE LAS IMÁGENES SUBIDAS DESDE CKEDITOR EN ALUMNOS NO SALGAN ROTAS 🌟
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)