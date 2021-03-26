
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UsuarioForm(forms.ModelForm):
    
    
    #url_perfil = forms.CharField(initial="https",label="Perfil del usuario",required=False, strip=False)
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        print(Usuarios.objects.count())
        self.siguiente =int(Usuarios.objects.count())
        self.siguiente+=1
        print(self.siguiente)
        self.fields['url_perfil'].label = "Perfil del usuario"
        self.fields['url_perfil'].initial = "/usuarios/perfil_usuario/"+str(self.siguiente)
        #self.fields['url_perfil'].required = False
        #self.fields['url_perfil'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Usuarios
        #Con este ocultamos los campos
        widgets = { 'url_perfil': forms.HiddenInput()  }
        fields = ["id","username","telefono","email","imagen_perfil","url_perfil", "password"]
        #fields ='__all__'
        #exclude = ("url_perfil",) 
        help_texts = {'username': ""}


""" Aqui creamos el mismo formulario para usuario pero desde cero """

class usuarioForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)



















class EditarUsuarioForm(ModelForm):
    
    
    class Meta:
        model = Usuarios 
        fields = ["username","email","telefono","imagen_perfil","biografia","url_perfil"]
        #exclude = ["password1"]
        #fields = '__all__'

