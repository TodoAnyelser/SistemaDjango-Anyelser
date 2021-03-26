from django.urls import path, include
from .views import Perfil, Perfil_Usuario, Editar_Perfil
from django.conf import settings
from django.conf.urls.static import static

app_name = "usuarios"
urlpatterns = [
    
    path('Perfil/', Perfil, name='perfil'),
    path('perfil_usuario/<id_perfil>', Perfil_Usuario, name='perfil_usuario'),
    path('editar_perfil/<id_perfil>/', Editar_Perfil, name='editar_perfil'),
    
]
