from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class Usuarios(AbstractUser):
    
    first_name=None
    last_name=None
    id = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    imagen_perfil = models.ImageField(upload_to ='usuarios/perfil/',null=True) 
    biografia = models.TextField(blank=True)
    url_perfil = models.CharField(max_length=200, null=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'





