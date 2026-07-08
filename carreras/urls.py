from django.urls import path
from . import views

app_name = 'carreras' 

urlpatterns = [
    path('', views.lista_carreras, name='lista_carreras'),
    path('<slug:slug>/', views.detalle_carrera, name='detalle_carrera'),
]