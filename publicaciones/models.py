from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, Group
from django.db.models import DateTimeField
#from django.contrib.postgres.fields import ArrayField, DateTimeRangeField, IntegerRangeField
import os


class publicacion(models.Model):

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.CharField(max_length=600, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    url_perfil_usuario = models.CharField(max_length=200, null=True)
    archivo = models.FileField(upload_to="publicaciones/", null=True, blank=True)

    def __str__(self):
        return self.texto

    class Meta:
        ordering = ['-fecha_creacion']
