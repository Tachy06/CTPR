from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Anuncios(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='anuncios/',null=False, blank=True)
    contenido = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'
    
    def __str__(self):
        return self.titulo