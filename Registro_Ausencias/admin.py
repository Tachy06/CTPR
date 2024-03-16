from django.contrib import admin
from .models import *

# Register your models here.

class seccionAdmin(admin.ModelAdmin): # Se carga la tabla de Secciones en el panel admin para agregar las secciones desde ahí o modificarlas o borrarlas
    list_display = ['seccion']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'

class estudiantesAdmin(admin.ModelAdmin): # Se carga la tabla de Estudiantes en el panel admin para agregar los estudiantes desde ahí o modificarlas o borrarlas
    list_display = ['nombre_estudiante']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ['nombre_estudiante']

admin.site.register(secciones, seccionAdmin)
admin.site.register(estudiantes, estudiantesAdmin)