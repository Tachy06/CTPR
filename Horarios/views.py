from django.shortcuts import render
from .models import nivel
from Registro_Ausencias.models import *
# Create your views here.

def horarios(request):
    niveles = nivel.objects.all()
    seccion = secciones.objects.all()

    context = {
        'niveles': niveles,
        'secciones': seccion,
    }

    return render(request, 'horarios.html', context)