from django.contrib import admin
from .models import *

# Register your models here.

class especialidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    search_fields = ['nombre']

admin.site.register(Especialidad, especialidadAdmin)