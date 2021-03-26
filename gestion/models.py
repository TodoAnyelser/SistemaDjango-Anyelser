from django.db import models

# Create your models here.

class objetivos(models.Model):

    nombre = models.CharField(max_length=600, blank=True, null=True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    valor = models.IntegerField()
    

    def __str__(self):
        return "Objetivo: ",self.nombre


class Palancas(models.Model):
    objetivoId = models.ForeignKey(objetivos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=600, blank=True, null=True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    valor = models.IntegerField()

    def __str__(self):
        return "Palanca: ",self.nombre

class Experimentos(models.Model):
    PalancaId = models.ForeignKey(Palancas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=600, blank=True, null=True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    valor = models.IntegerField()

    def __str__(self):
        return "Experimento: ",self.nombre
