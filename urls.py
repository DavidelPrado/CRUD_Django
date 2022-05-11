from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('infomacion', views.informacion, name='informacion'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),
    path('borrar/<int:DNI>', views.borrar, name='borrar'),
    path('usuarios/editar/<int:DNI>', views.editar, name='editar'),
]