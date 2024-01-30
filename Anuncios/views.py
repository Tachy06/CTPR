from django.shortcuts import render
from .models import *

# Create your views here.

def anuncios(request):
    anuncio = Anuncios.objects.all()
    contexto = {'anuncios':anuncio}
    return render(request, 'anuncios.html', contexto)
