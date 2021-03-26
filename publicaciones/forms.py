from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from usuarios.models import *
import datetime



class PublicacionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(PublicacionForm, self).__init__(*args, **kwargs)
        print("Entramos en formulario PublicacionForm")

        #self.fields['autor'].queryset = Usuarios.objects.filter(id=usuario.id)
        #self.fields['autor'].empty_label = None
        #url_completa=usuario.url_perfil+str(usuario.id)
        
        #self.fields['url_perfil_usuario'].initial = url_completa


    class Meta:
        model = publicacion
        widgets = {'texto': forms.Textarea(attrs={'cols': 90, 'rows': 5}), 'url_perfil_usuario': forms.HiddenInput()  }
        labels = {
            'texto': '', 'archivo':'',
        }
        help_texts = {
            'texto': ('Ingresa lo que quieras'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
        }
        #fields = "__all__"
        exclude ={ 'autor','url_perfil_usuario'}


#Estamos usando ESTE POR AHORA
class PublicacionForm2(forms.Form):
    
    #autor = forms.Choi .ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = forms.CharField(error_messages={'required': 'Por favor ingresa tu publicacion'},label='Publicacion',max_length=600,required=True,help_text='600 CARACTERES MAXIMO')
    fecha_creacion = forms.DateField(initial=datetime.date.today)
    #url_perfil = forms.URLField(max_length=200, required=False)
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(PublicacionForm2, self).__init__(*args, **kwargs)
        print("SOY EL USUARIO", usuario)
        url_completa=usuario.url_perfil+str(usuario.id)
        print("MI URL", usuario.url_perfil)
        self.fields['url_perfil_usuario'].initial = url_completa

    class Meta:
        model = publicacion
        widgets = { 'url_perfil_usuario': forms.HiddenInput()  }
        fields = "__all__"