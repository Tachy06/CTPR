from django.contrib import admin
from .models import *

# Register your models here.

class seccionAdmin(admin.ModelAdmin):
    list_display = ['seccion']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'

class estudiantesAdmin(admin.ModelAdmin):
    list_display = ['nombre_estudiante']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ['nombre_estudiante']

admin.site.register(secciones, seccionAdmin)
admin.site.register(estudiantes, estudiantesAdmin)