from django.db import models

# Create your models here.

class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100,blank=True,default='')
    code = models.TextField()
    es_valido = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
