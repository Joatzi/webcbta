from django.contrib import admin
from .models import Carrera, ImagenCarrera


class ImagenCarreraInline(admin.TabularInline):
    model = ImagenCarrera
    extra = 3 

class CarreraAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'duracion')
    search_fields = ('titulo', 'resumen')
    
    # 🔽 AGREGAMOS ESTA LÍNEA 🔽
    inlines = [ImagenCarreraInline]

admin.site.register(Carrera, CarreraAdmin)