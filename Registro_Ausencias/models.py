from django.db import models
from Horarios.models import *

# Create your models here.

class secciones(models.Model):
    seccion = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='horarios/', null=False, blank=True)
    nivel = models.ForeignKey(nivel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    verbose_name = 'Seccion'
    verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return self.seccion

class estudiantes(models.Model):
    nombre_estudiante = models.CharField(max_length=200)
    seccion_estudiante = models.ManyToManyField(secciones)
    nombre_padre = models.CharField(max_length=200)
    correo_padre = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return self.nombre_estudiante