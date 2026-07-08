from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path("blog/", include("blog.urls")),

    path('carreras/', include('carreras.urls')),
    
    path('ckeditor5/', include('django_ckeditor_5.urls')),

    path('alumnos/', include('alumnos.urls')),

    path("", include("web.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
