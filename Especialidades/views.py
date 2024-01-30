from django.shortcuts import render
from .models import *

# Create your views here.

def especialidades(request):
    especi = Especialidad.objects.all()
    contexto = {'especi':especi}
    return render(request, 'especialidades.html', contexto)


def vistaEspecialidad(request, slug_text):
    slug = Especialidad.objects.filter(slug=slug_text)
    contexto = {'especialidades':slug}
    return render(request, 'especialidad.html', contexto)