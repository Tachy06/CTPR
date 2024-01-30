from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('viewPreMatricula/', viewPreMatricula, name='ViewPreMatricula'),
    path('PreMatricula/', downloadPreMatricula, name='DownloadPreMatricula'),
    path('pdf/', html_to_pdf.as_view(), name='html_to_pdf'),
]
if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)