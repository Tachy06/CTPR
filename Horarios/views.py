from django.shortcuts import render
from .models import nivel
from Registro_Ausencias.models import *
# Create your views here.

def horarios(request):
    niveles = nivel.objects.all() # Se carga todos los niveles que hay, por ejemplo: Séptimo, octavo, noveno, etc...
    seccion = secciones.objects.all() # Se carga todos los secciones que hay

    context = {
        'niveles': niveles,
        'secciones': seccion,
    } # Se pasan al html

    return render(request, 'horarios.html', context)