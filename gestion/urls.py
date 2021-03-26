from django.shortcuts import render
from django.urls import path, include
from . import views
from django.conf import settings

app_name="gestiones"
urlpatterns = [
    
    path('Prueba/', views.Pedidos, name='prueba1'),
    
    #path('lista_publicaciones/', views.lista_publicaciones, name='listaPublicaciones'),
    #path('editar_publicaciones/<id_publicacion>/', views.editar_publicaciones, name='editar_publicaciones'),
    #path('borrar_Publicaciones/<id_publicacion>/', views.borrar_Publicaciones, name='borrar_Publicaciones')
]
