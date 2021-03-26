from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def Perfil(request):
    
    unico=Usuarios.objects.get(id=request.user.id)
    print(unico)
    print(unico.id)
    print(unico.telefono)
    print(unico.biografia)
    print(unico.url_perfil)
    print(unico.imagen_perfil)
    print(" ")
    print(" ")
    
    contexto={'MiUsuario':unico}
    return render(request,"usuarios/perfil.html",contexto)


def Perfil_Usuario(request,id_perfil):
   
   
    esIgual=False
    perfil_usuario=Usuarios.objects.get(id=id_perfil)
    print("perfil del usuario al que entraras: ",perfil_usuario," y su id es:", perfil_usuario.id," tu id de usuario es:",request.user.id)
    if perfil_usuario.id == request.user.id:
        esIgual=True
    else:
        esIgual=False
    print(perfil_usuario)
    contexto={'MiUsuario':perfil_usuario,'PerfilPersonal':esIgual}
    
    return render(request,"usuarios/perfil_usuario.html",contexto)


def Editar_Perfil(request,id_perfil):
    

    #user = Usuarios.objects.get(id=id_perfil)
    #user.set_password('0000')
    #user.save()

    # Recuperamos la instancia de la persona
    instancia = Usuarios.objects.get(id=id_perfil)

    # Creamos el formulario con los datos de la instancia
    form = EditarUsuarioForm(instance=instancia)
    
    contexto={'formularioUsuarios':form}

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = EditarUsuarioForm(request.POST, request.FILES, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
        form=EditarUsuarioForm()
        contexto= {'formularioUsuarios':form}

    return render(request,"usuarios/editar_perfil.html",contexto)