from django.shortcuts import render
from Principal.models import *
from django.views.generic import View

# Create your views here.

def viewPreMatricula(request):
    if request.method == 'POST':
        cedu_estu = request.POST['cedulaEstu']
        request.session['cedu_estu'] = cedu_estu
        estudiante = preMatricula.objects.filter(cedu_estudiante=cedu_estu)
        return render(request, 'downloadPreMatricula.html', {'estudiante':estudiante})
    else:
        return render(request, 'view-prematricula.html')

def downloadPreMatricula(request):
    return render(request, 'downloadPreMatricula.html')

class html_to_pdf(View):
    def get(self, request, *args, **kwargs):
        cedu_estu = request.session.get('cedu_estu', None)
        if cedu_estu is not None:
            estudiante = preMatricula.objects.filter(cedu_estudiante=cedu_estu)
            data = {
                'estudiante': estudiante
            }
            pdf = render_to_pdf('../templates/viewpdf.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            # Manejar el caso en el que la cédula no está en la sesión
            return HttpResponse("Cédula no encontrada en la sesión. ¿Olvidó completar el formulario previamente?")
    