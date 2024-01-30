from django.contrib import admin
from .models import *

# Register your models here.

class nivelesAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

admin.site.register(nivel, nivelesAdmin)