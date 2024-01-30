from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', registroAusencias, name='Ausencias'),
    path('estudiantes/<slug:seccion_slug>/', estudiantesAusentes, name='Estudiantes'),
]
if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)