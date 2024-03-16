from django.db import models
from ckeditor.fields import RichTextField
from CTPR.utils import *
from django.db.models.signals import pre_save
# Create your models here.

class Especialidad(models.Model): # Se crea la tabla de las especialidades con todos sus campos
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='especialidades/',null=False, blank=True)
    contenido = RichTextField()
    slug = models.SlugField(max_length=200, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nombre
    
def slug_generator(sender, instance, *arg, **kwargs): # Se hace la lógica del slug para cada especialidad
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Especialidad)