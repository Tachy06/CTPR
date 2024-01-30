from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='Home'),
    path('ubicacion/', ubicacion, name='Ubicacion'),
    path('acercaDe/', acercaDe, name='AcercaDe'),
    path('valores/', valores, name='Valores'),
    # path('horarios/', horarios, name='Horarios'),
    path('prematricula10/', preMatricula10, name="PreMatricula10"),
    path('contacto/', contacto, name='Contacto'),
]
if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)