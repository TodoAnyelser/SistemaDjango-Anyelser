


from django.shortcuts import render, redirect
from .models import publicacion
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import * 
from publicaciones.forms import *
from usuarios.models import Usuarios
import os
from datetime import date
from datetime import datetime



def home(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        
        if request.method == "GET":

            print("\nENTRAMOS A GET DE HOME con el usuario: ", request.user,"\n")
            
            #Día actual
            today = date.today()

            #Fecha actual
            now = datetime.now()
            #print(" ")
            #print("HOY ES: ",today.day)
            #print("Fecha actual: ",now)
            #print(" ")
            Cantidad = publicacion.objects.filter(autor_id=request.user.id,fecha_creacion__day=today.day)

            TotalPublicaciones = Cantidad.count()
            if TotalPublicaciones>1:
                print("SERA PUBLICACION")
                palabra="Publicacion"
            else:
                if TotalPublicaciones ==0:
                    palabra="Publicaciones"
                else:
                    palabra="Publicacion"

            if TotalPublicaciones<=10:
                form=PublicacionForm(usuario=request.user)
                print("Enviaremos un formulario completo")
            else:
                form=None
                print("Pasaremos un form nulo")
            """ESTE ES DE PRUEBA"""
            #form = PublicacionForm2(usuario=request.user)

            print(form)
            publicaciones = publicacion.objects.all()
            contexto= {'formularioPublicaciones':form,'publicaciones':publicaciones,'TotalPublicaciones':TotalPublicaciones,'palabraPublicacion':palabra}
            return render(request,"publicaciones/index.html",contexto)


        if request.method == "POST":
            
            print("\nENTRAMOS A POST DE HOME con el usuario: ", request.user,"\n")
            # Añadimos los datos recibidos al formulario
            form = PublicacionForm(request.POST,usuario=request.user)
            #form = PublicacionForm2(request.POST, request.FILES)
            No_media=request.POST
            ARCHIVO=request.FILES['archivo']
            # Si el formulario es válido...
            if form.is_valid():
                
                
                usuario=Usuarios.objects.get(id=request.user.id)
                probando = publicacion(autor=usuario, texto=request.POST['texto'], archivo=ARCHIVO)
                print("SE GUARDO LA PUBLICACION")
                print(probando)
                probando.save()

                #Día actual
                today = date.today()
                Cantidad = publicacion.objects.filter(autor_id=request.user.id,fecha_creacion__day=today.day)

                #print("ESTAMOS PROBANDO",Cantidad.count())
                TotalPublicaciones = Cantidad.count()

                if TotalPublicaciones>1:
                    palabra="Publicaciones"
                else:
                    if TotalPublicaciones ==0:
                        palabra="Publicaciones"
                    else:
                        palabra="Publicacion"

                if TotalPublicaciones<=10:
                    form=PublicacionForm(usuario=request.user)
                else:
                    form=None
                """ESTE ES DE PRUEBA"""
                #form = PublicacionForm2(usuario=request.user)
                contexto= {'formularioPublicaciones':form,'publicaciones':publicacion.objects.all(),'TotalPublicaciones':TotalPublicaciones,'palabraPublicacion':palabra}
                return render(request, "publicaciones/index.html",contexto)
            
            else:
                print("No se pudo procesar el archivo")
                print(form)
                contexto= {'formularioPublicaciones':form,'publicaciones':publicacion.objects.all(),'TotalPublicaciones':TotalPublicaciones,'palabraPublicacion':palabra}
                return render(request, "publicaciones/index.html",contexto)

#Este else es de autenticate
    else:
        print("El usuario no esta autenticado")           
        # En otro caso redireccionamos al login
        return redirect('/login')


def lista_publicaciones(request):

    return render(request,"lista_publicaciones.html")

def editar_publicaciones(request,id_publicacion):

    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:

        # Recuperamos la instancia de la persona
        instancia = publicacion.objects.get(id=id_publicacion)

        # Creamos el formulario con los datos de la instancia
        form = PublicacionForm(instance=instancia,usuario=request.user)
        
        contexto={'formularioPublicaciones':form}

        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Actualizamos el formulario con los datos recibidos
            form = PublicacionForm(request.POST, instance=instancia,usuario=request.user)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
            form=PublicacionForm(usuario=request.user)
            publicaciones = publicacion.objects.all()
            contexto= {'formularioPublicaciones':form,'publicaciones':publicaciones}
            return render(request,"publicaciones/index.html",contexto)

        print("la publicacion escogida es:",id_publicacion,contexto)
        return render(request,"publicaciones/editar_publicacion.html",contexto)

    else:
        print("El usuario no esta autenticado")           
        # En otro caso redireccionamos al login
        return redirect('/login')


def borrar_Publicaciones(request, id_publicacion):

    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        # Recuperamos la instancia de la persona y la borramos
        instancia = publicacion.objects.get(id=id_publicacion)
        instancia.delete()

        # Después redireccionamos de nuevo a la lista
        form=PublicacionForm(usuario=request.user)
        publicaciones = publicacion.objects.all()
        contexto= {'formularioPublicaciones':form,'publicaciones':publicaciones}
        return render(request,"publicaciones/index.html",contexto)

    else:
        print("El usuario no esta autenticado")           
        # En otro caso redireccionamos al login
        return redirect('/login')


def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UsuarioForm()
    print(form)
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UsuarioForm(request.POST, request.FILES)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    
    #form.fields['username'].help_text = None
    #form.fields['password1'].help_text = None
    #form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/registro.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

