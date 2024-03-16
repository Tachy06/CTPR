from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
# Create your views here.

def registroAusencias(request):
    if request.method == 'POST':
        seccion_slug = request.POST['secciones']
        if seccion_slug == '0': # Si no se selecciona una sección muestra un mensaje de error y redirecciona a la misma página
            messages.error(request, 'Seleccione una sección')
            return redirect('/ausencias/')
        else:
            if seccion_slug:
                return redirect(f'estudiantes/{seccion_slug}/', seccion_slug=seccion_slug) # Si si se selecciona entonces redirige a esa sección
    else:
        seccion = secciones.objects.all() # Se carga todas las secciones para mostrarlas
        contexto = {'secciones': seccion}
        return render(request, 'ausencias.html', contexto)
    
def estudiantesAusentes(request, seccion_slug):
    if request.method == 'POST':
        selected_students = request.POST.getlist('estudianteAusente')
        nombre_profesor = request.POST['nombre_profesor']
        materia = request.POST['materia']
        if nombre_profesor == '': # Si a la hora de reportar a un estudiante no se escribe quien lo reporta va a mostrar un error
            messages.error(request, 'Nombre del profesor es requerido')
            return redirect(f'/ausencias/estudiantes/{seccion_slug}/')
        elif materia == '': # Si se deja en blanco el nombre de la materia muestra un mensaje de error
            messages.error(request, 'Materia es requerida')
            return redirect(f'/ausencias/estudiantes/{seccion_slug}/')
        elif nombre_profesor.isspace(): # Verifica que no haya solo espacios en blanco y si los hay muestra un mensaje de error
            messages.error(request, 'Nombre del profesor es requerido')
            return redirect(f'/ausencias/estudiantes/{seccion_slug}/')
        elif materia.isspace(): # Verifica que no haya solo espacios en blanco y si los hay muestra un mensaje de error
            messages.error(request, 'Materia es requerida')
            return redirect(f'/ausencias/estudiantes/{seccion_slug}/')
        for students_id in selected_students: # Va uno a uno de los estudiantes seleccionados y les envia el correo al Email guardado de los padres en la base de datos
            student = estudiantes.objects.get(id=students_id) # Se busca el estudiante mediante el id obtenido
            comentario_opcional = request.POST.get(f'comentario_{students_id}') # Se carga el mensaje opcional en una variable
            subject = "Comunicado urgente del Cotai hacia su hogar" # Se crea el subject para el correo
            message = f"Hola estimad@ {student.nombre_padre} por este medio, yo {nombre_profesor} profesor de la materia {materia} deseo comunicarle que su hijo tiene unas ausencias en mi clase \n{comentario_opcional} \nSaludos Cordiales" # Se crea el cuerpo del correo
            from_email = "web.cotai.sc@gmail.com" # Quien lo manda
            to_email = student.correo_padre # Hacia donde se manda
            send_mail(subject, message, from_email, [to_email], fail_silently=False,) # Se envía el correo
        return redirect('/') # Se redirecciona a la página principal
    else:
        section = secciones.objects.get(seccion=seccion_slug) # Se carga la sección dependiendo cual se seleccionó
        students = estudiantes.objects.filter(seccion_estudiante=section) # Se cargan todos lso estudiantes de esa sección
        disable = False
        if students.exists():
            contexto = {'estudiantes': students, 'section':section}
            return render(request, 'estudiantes.html', contexto)
        else:
            disable = True
            contexto = {'disable':disable}
            return render(request, 'estudiantes.html', contexto)