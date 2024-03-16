from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *
from .models import preMatricula, showPrematricula
from datetime import datetime
from django.utils.crypto import get_random_string

# Create your views here.

def home(request):
    show = showPrematricula.objects.last()
    contexto = {'show': show}
    return render(request, 'index.html', contexto) # Se carga el html index del proyecto

def ubicacion(request):
    contexto = {}
    return render(request, 'ubicacion.html', contexto) # Se carga el html donde se encuentra la ubicación por google maps y escrita del colegio

def acercaDe(request):
    return render(request, 'acercaDe.html') # Se carga el html donde se habla un poco sobre la institución

def valores(request):
    return render(request, 'valores.html') # Se carga el html donde se habla un poco sobre los valores que tienen tantos los estudiantes, profesores y administradores en la institución

def horarios(request):
    return render(request, 'horarios.html') # Este es el html donde se carga los horarios de todas las secciones del colegio, la lógica para cargar las fotos desde el panel se hace desde el html puro

def contacto(request):
    if request.method == 'POST': # Se pregunta si se hizo la petición de tipo POST
        correo = request.POST['inpCorreo'] # Se obtiene el value del campo inpCorreo
        consulta = request.POST['consultas'] # Se obtiene el value del campo consultas
        if consulta == 'Motivo':
            messages.error(request, 'Elije el motivo')
            return redirect('/contacto/') # Se valida si consulta es igual a Motivo, ya que es la que viene por defecto y no se puede mandar así y si es así redirecciono de nuevo a la página contacto y muestro un mensaje de error
        else:
            mensaje = request.POST['areaMensaje'] # Se obtiene el value del campo areaMensaje
            subject = 'Mensaje de parte de la página web' # Se redacta el subject que va a tener el correo
            message = f'Proveniente de: {correo} \nMotivo: {consulta} \nMensaje: {mensaje}' # Se redacta el mensaje que va a tener el correo
            from_email = str(correo) # Se define hacia donde va hacer enviado
            to_email = 'web.cotai.sc@gmail.com' # se define quien lo va a enviar 
            send_mail(subject, message, from_email, [to_email], fail_silently=False,) # Se envia el correo con las configuraciones anteriores
            return redirect('/')
    else:
        return render(request, 'contact.html') # Cargo el html de contacto para el GET, osea para mostrarlo simplemente

def preMatricula10(request):
    if request.method == "POST":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@-#$%&1234567890" # Se define que caracteres se van a usar para generar el token en la prematricula
        token = get_random_string(length=30, allowed_chars=characters) # Se genera el token de la prematricula
        # A continuación se obtienen todos los valores obtenidos en los inputs
        typeIdentification = request.POST['typeIdentification']
        typeIdentificationDad = request.POST['typeIdentificationDad']
        especialidadesSeleccionadas = request.POST.getlist('especialidadSelect')

        #* Datos del estudiante
        cedulaEstu = request.POST['ceduEstu']
        nombre_estu = request.POST['nameEstu']
        nacionalidad_estu = request.POST['nacionalidadEstu']
        fecha_estu = request.POST['dateofbirth']
        email_Estu = request.POST['emailEstu']
        sexo_estu = request.POST['RadioSexo']
        instituto = request.POST['instituto']
        repitencia = request.POST['RadioRepe']
        print(str(cedulaEstu) + ' - ' + nombre_estu + ' - ' + nacionalidad_estu + ' - ' + str(fecha_estu)  + ' - ' +
            email_Estu + ' - ' + sexo_estu + ' - ' + instituto + ' - ' + repitencia)

        #* Datos de la especialidad
        especialidad_values = ""
        for especialidad_id in especialidadesSeleccionadas:
            especialidad = Tecnicas.objects.get(id=especialidad_id)
            especialidad_values += str(especialidad) + ' - '
        especialidad_favorita = request.POST['especialidadFavorita']

        #* Datos del padre
        cedulaDad = request.POST['IDdad']
        nombre_padre = request.POST['nameDad']
        nacionalidad_padre = request.POST['nacionalidadDad']
        radio_padre = request.POST['RadioSexoDad']
        telefono_padre = request.POST['Tele']
        correo_padre = request.POST['correoPadre']
        ocupacion = request.POST['ocupacion']
        print(cedulaDad + ' - ' + nombre_padre + ' - ' + nacionalidad_padre + ' - ' + radio_padre + ' - ' + telefono_padre +
                ' - ' + correo_padre + ' - ' + ocupacion)
        fecha_atual = datetime.now() # Se obtiene la fecha actual
        fecha_date = datetime.strptime(fecha_estu, '%Y-%m-%d') # Se cambia a formato de '1/1/2024'
        day = fecha_date.day # Se obtiene nada mas el día actual
        month = fecha_date.month # Se obtiene nada mas el mes actual
        year = fecha_date.year # Se obtiene nada mas el año actual
        fecha_datetime = datetime(year, month, day) # Se coloca todo en una sola fecha
        if fecha_datetime >= fecha_atual: # Se compara si la fecha actual y la obtenida del usuario es la misma y si es así da un mensaje de error
            messages.error(request, 'La fecha de nacimiento no puede ser hoy o días después de hoy')
            return redirect('/prematricula10/')
        cedu_buscada = preMatricula.objects.filter(cedu_estudiante=cedulaEstu) # Se hace una busqueda en la base de datos para averiguar si el estudiante ya tiene una prematricula en cola
        if cedu_buscada.exists(): # Pregunta si existe y si es así muestrame un mensaje de error
            messages.error(request, 'Esta persona ya tiene una PreMatricula en curso')
            return redirect('/prematricula10/')
        if typeIdentification == '1':
            if len(cedulaEstu) != 9: # Si es mayor o menor a 9 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula invalida, debe ser de 9 caracteres')
                    return redirect('/prematricula10/')
            elif typeIdentificationDad == '1': # Se pregunta si el tipo de identificación es 1 osea si es nacional, esto para el padre
                if len(cedulaDad) != 9: # Si es mayor o menor a 9 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula de padre invalida, debe ser de 9 caracteres')
                    return redirect('/prematricula10/')
                elif cedulaEstu == cedulaDad: # Se pregunta si la cédula del padre y del hijo son iguales, si lo son por obvias razones no se deja ingresar
                    messages.error(request, 'La cédula del padre no puede ser igual a la del hijo')
                    return redirect('/prematricula10/')
                else:
                    preMatricula.objects.create(nombre_estudiante=nombre_estu, cedu_estudiante=int(cedulaEstu),
                        nacionalidad_estudiante=nacionalidad_estu, fecha_estudiante=fecha_estu,
                        correo_estudiante=email_Estu, sexo_estudiante=sexo_estu, colegio_procedencia=instituto, repitencia=repitencia,
                        especialidades=especialidad_values, especialidadFavorita=especialidad_favorita,
                        nombre_padre=nombre_padre, cedu_padre=int(cedulaDad), nacionalidad_padre=nacionalidad_padre,
                        sexo_padre=radio_padre, telefono_padre=int(telefono_padre), correo_padre=correo_padre,
                        ocupacion_padre=ocupacion, token=token)
                    messages.success(request, 'Prematricula realizada')
                    return redirect('/prematricula10/') # Si todo es válido se registra en base de datos
            elif typeIdentificationDad == '2':
                if len(cedulaDad) != 12: # Si es mayor o menor a 12 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula de padre invalida, debe ser de 12 caracteres')
                    return redirect('/prematricula10/')
                elif cedulaEstu == cedulaDad: # Se pregunta si la cédula del padre y del hijo son iguales, si lo son por obvias razones no se deja ingresar
                    messages.error(request, 'La cédula del padre no puede ser igual a la del hijo')
                    return redirect('/prematricula10/')
                else:
                    preMatricula.objects.create(nombre_estudiante=nombre_estu, cedu_estudiante=int(cedulaEstu),
                        nacionalidad_estudiante=nacionalidad_estu, fecha_estudiante=fecha_estu,
                        correo_estudiante=email_Estu, sexo_estudiante=sexo_estu, colegio_procedencia=instituto, repitencia=repitencia,
                        especialidades=especialidad_values, especialidadFavorita=especialidad_favorita,
                        nombre_padre=nombre_padre, cedu_padre=int(cedulaDad), nacionalidad_padre=nacionalidad_padre,
                        sexo_padre=radio_padre, telefono_padre=int(telefono_padre), correo_padre=correo_padre,
                        ocupacion_padre=ocupacion, token=token)
                    messages.success(request, 'Prematricula realizada')
                    return redirect('/prematricula10/') # Si todo es válido se registra en base de datos
            elif typeIdentificationDad == '0': # Si es igual a 0 el tipo de cédula significa que no seleccionó ninguna cédula
                messages.info(request, 'Selecciona un tipo de cédula')
                return redirect('/prematricula10/')
                
        elif typeIdentification == '2':
            if len(cedulaEstu) != 12: # Si es mayor o menor a 12 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula invalida, debe ser de 12 caracteres')
                    return redirect('/prematricula10/')
            elif typeIdentificationDad == '1':
                if len(cedulaDad) != 9: # Si es mayor o menor a 9 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula de padre invalida, debe ser de 9 caracteres')
                    return redirect('/prematricula10/')
                elif cedulaEstu == cedulaDad: # Se pregunta si la cédula del padre y del hijo son iguales, si lo son por obvias razones no se deja ingresar
                    messages.error(request, 'La cédula del padre no puede ser igual a la del hijo')
                    return redirect('/prematricula10/')
                else:
                    preMatricula.objects.create(nombre_estudiante=nombre_estu, cedu_estudiante=int(cedulaEstu),
                        nacionalidad_estudiante=nacionalidad_estu, fecha_estudiante=fecha_estu,
                        correo_estudiante=email_Estu, sexo_estudiante=sexo_estu, colegio_procedencia=instituto, repitencia=repitencia,
                        especialidades=especialidad_values, especialidadFavorita=especialidad_favorita,
                        nombre_padre=nombre_padre, cedu_padre=int(cedulaDad), nacionalidad_padre=nacionalidad_padre,
                        sexo_padre=radio_padre, telefono_padre=int(telefono_padre), correo_padre=correo_padre,
                        ocupacion_padre=ocupacion, token=token)
                    messages.success(request, 'Prematricula realizada')
                    return redirect('/prematricula10/') # Si todo es válido se registra en base de datos
            elif typeIdentificationDad == '2':
                if len(cedulaDad) != 12: # Si es mayor o menor a 12 digitos da un error ya que es una cédula no valida y da un mensaje de error
                    messages.error(request, 'Cédula de padre invalida, debe ser de 12 caracteres')
                    return redirect('/prematricula10/')
                elif cedulaEstu == cedulaDad: # Se pregunta si la cédula del padre y del hijo son iguales, si lo son por obvias razones no se deja ingresar
                    messages.error(request, 'La cédula del padre no puede ser igual a la del hijo')
                    return redirect('/prematricula10/')
                else:
                    preMatricula.objects.create(nombre_estudiante=nombre_estu, cedu_estudiante=int(cedulaEstu),
                        nacionalidad_estudiante=nacionalidad_estu, fecha_estudiante=fecha_estu,
                        correo_estudiante=email_Estu, sexo_estudiante=sexo_estu, colegio_procedencia=instituto, repitencia=repitencia,
                        especialidades=especialidad_values, especialidadFavorita=especialidad_favorita,
                        nombre_padre=nombre_padre, cedu_padre=int(cedulaDad), nacionalidad_padre=nacionalidad_padre,
                        sexo_padre=radio_padre, telefono_padre=int(telefono_padre), correo_padre=correo_padre,
                        ocupacion_padre=ocupacion, token=token)
                    messages.success(request, 'Prematricula realizada')
                    return redirect('/prematricula10/') # Si todo es válido se registra en base de datos
            elif typeIdentificationDad == '0': # Si es igual a 0 el tipo de cédula significa que no seleccionó ninguna cédula
                messages.info(request, 'Selecciona un tipo de cédula')
                return redirect('/prematricula10/')
        elif typeIdentification == '0': # Si es igual a 0 el tipo de cédula significa que no seleccionó ninguna cédula
            messages.info(request, 'Selecciona un tipo de cédula')
            return redirect('/prematricula10/')
    else:
        show = showPrematricula.objects.last()
        tecnicas = Tecnicas.objects.all()
        contexto = {'tecnicas': tecnicas, 'show': show}
        return render(request, 'preMatricula10.html', contexto) # Se carga el html de la prematricula con las tecnicas que hay registradas en la tabla de Tecnicas