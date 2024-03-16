from django.contrib import admin
from .models import *

# Register your models here.

class tecnicasAdmin(admin.ModelAdmin): # Se carga la tabla de Tecnicas en el panel admin para agregar las técinas desde ahí o modificarlas o borrarlas
    list_display = ['nombre']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ['nombre']

class preMatriculaAdmin(admin.ModelAdmin): # Se carga la tabla de Prematricila en el panel admin para agregar los estudiantes desde ahí o modificarlas o borrarlas
    list_display = ['cedu_estudiante', 'nombre_estudiante']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ['cedu_estudiante', 'nombre_estudiante', 'token']

class showPrematriculaAdmin(admin.ModelAdmin): # Se carga la tabla de showPrematricila en el panel admin para permitir si mostrar la prematricula o no
    list_display = ['show']

admin.site.register(Tecnicas, tecnicasAdmin)
admin.site.register(preMatricula, preMatriculaAdmin)
admin.site.register(showPrematricula, showPrematriculaAdmin)