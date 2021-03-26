
from django.shortcuts import render
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="publicaciones"
urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('lista_publicaciones/', views.lista_publicaciones, name='listaPublicaciones'),
    path('editar_publicaciones/<id_publicacion>/', views.editar_publicaciones, name='editar_publicaciones'),
    path('borrar_Publicaciones/<id_publicacion>/', views.borrar_Publicaciones, name='borrar_Publicaciones'),
    path('register', views.registro),
    path('login', views.login),
    path('logout', views.logout),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

