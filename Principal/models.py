from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from CTPR.utils import *

# Create your models here.

class Tecnicas(models.Model): # Es la tabla para registrar las tenicas habidas en el colegio para la prematricula de décimo
    nombre = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    verbose_name = 'Tecnica'
    verbose_name_plural = 'Tecnicas'
    
    def __str__(self):
        return self.nombre

class preMatricula(models.Model): # Es la tabla para registrar a los estudiantes para la prematricula   
    nombre_estudiante = models.CharField(max_length=255, null=False)
    cedu_estudiante = models.BigIntegerField(null=False)
    nacionalidad_estudiante = models.CharField(max_length=255, null=False)
    fecha_estudiante = models.DateField(max_length=255, null=False)
    correo_estudiante = models.EmailField(null=False)
    sexo_estudiante = models.CharField(max_length=255, null=False)
    colegio_procedencia = models.CharField(max_length=100, null=False)
    repitencia = models.CharField(max_length=10, null=False)
    especialidades = models.CharField(max_length=500, null=False)
    especialidadFavorita = models.CharField(max_length=255, null=False)
    nombre_padre = models.CharField(max_length=255, null=False)
    cedu_padre = models.BigIntegerField(null=False)
    nacionalidad_padre = models.CharField(max_length=255, null=False)
    sexo_padre = models.CharField(max_length=255, null=False)
    telefono_padre = models.IntegerField(null=False)
    correo_padre = models.EmailField(null=False)
    ocupacion_padre = models.CharField(max_length=255, null=False)
    token = models.CharField(max_length=30, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Prematricula'
        verbose_name_plural = 'Prematriculas'

    def __int__(self):
        return self.cedu_estudiante
    
class showPrematricula(models.Model):
    show = models.BooleanField(default=False, null=False)

    class Meta:
        verbose_name = 'showPrematricula'
        verbose_name_plural = 'showPrematriculas'

    def __int__(self):
        return self.show