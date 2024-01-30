from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
# Create your views here.

def registroAusencias(request):
    if request.method == 'POST':
        seccion_slug = request.POST['secciones']
        if seccion_slug == '0':
            messages.error(request, 'Seleccione una sección')
            return redirect('/ausencias/')
        else:
            if seccion_slug:
                return redirect(f'estudiantes/{seccion_slug}/', seccion_slug=seccion_slug)
    else:
        seccion = secciones.objects.all()
        contexto = {'secciones': seccion}
        return render(request, 'ausencias.html', contexto)
    
def estudiantesAusentes(request, seccion_slug):
    if request.method == 'POST':
        selected_students = request.POST.getlist('estudianteAusente')
        nombre_profesor = request.POST['nombre_profesor']
        materia = request.POST['materia']
        if nombre_profesor == '':
                messages.error(request, 'Nombre del profesor es requerido')
                return redirect(f'/estudiantes/{seccion_slug}/')
        else:
            if materia == '':
                messages.error(request, 'Materia es requerida')
                return redirect(f'/estudiantes/{seccion_slug}/')
            else:
                if nombre_profesor == ' ':
                        messages.error(request, 'Nombre del profesor es requerido')
                        return redirect(f'/estudiantes/{seccion_slug}/')
                else:
                    if materia == ' ':
                        messages.error(request, 'Materia es requerida')
                        return redirect(f'/estudiantes/{seccion_slug}/')
        for students_id in selected_students:
            student = estudiantes.objects.get(id=students_id)
            comentario_opcional = request.POST.get(f'comentario_{students_id}')
            print(student)
            subject = "Comunicado urgente del Cotai hacia su hogar"
            message = f"Hola estimad@ {student.nombre_padre} esto es una prueba de parte del profesor {nombre_profesor} de la materia {materia} \n{comentario_opcional}"
            from_email = "kendallrodri1@gmail.com"
            to_email = student.correo_padre
            send_mail(subject, message, from_email, [to_email], fail_silently=False,)
        return redirect('/')
    else:
        section = secciones.objects.get(seccion=seccion_slug)
        students = estudiantes.objects.filter(seccion_estudiante=section)
        disable = False
        if students.exists():
            contexto = {'estudiantes': students, 'section':section}
            return render(request, 'estudiantes.html', contexto)
        else:
            disable = True
            contexto = {'disable':disable}
            return render(request, 'estudiantes.html', contexto)