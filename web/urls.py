from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("historia/", views.historia, name="historia"),
    path("mision/", views.mision, name="mision"),
    path("vision/", views.vision, name="vision"),
    path("blog/", views.blog, name="blog"),
    path("contacto/", views.contacto, name="contacto"),
    
]
