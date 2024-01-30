from django.contrib import admin
from .models import *

# Register your models here.
class anunciosAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    readonly_fields = ('fecha', )
    date_hierarchy = 'fecha'

admin.site.register(Anuncios, anunciosAdmin)
