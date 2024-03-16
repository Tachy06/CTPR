from django.shortcuts import render
from .models import *

# Create your views here.

def especialidades(request):
    especi = Especialidad.objects.all() # Se cargan todas las especialidades guardadas
    contexto = {'especi':especi} # Se pasan al html
    return render(request, 'especialidades.html', contexto)


def vistaEspecialidad(request, slug_text):
    slug = Especialidad.objects.filter(slug=slug_text) # Se obtiene la especialidad seleccionada y se crea la vista de esa especialidad
    contexto = {'especialidades':slug}
    return render(request, 'especialidad.html', contexto)