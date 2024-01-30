from django.db import models

# Create your models here.

class nivel(models.Model):
    nombre = models.CharField(max_length=255, null=False)

    verbose_name = 'Nivel'
    verbose_name_plural = 'Niveles'
    
    def __str__(self):
        return self.nombre