from rest_framework import serializers
from usuarios.models import Usuarios
from .models import Snippet


"""
Esto de aqui son ejemplos de la documentacion directa de MARCO DJANGO REST
"""

#Esta forma se hace con Serializer que seria como form
"""
class SnippetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    es_valido = serializers.BooleanField(required=False)

    def create(self, validated_data):
    
        #Crea y retorna un nuevo `Snippet` instance, given the validated data.
        
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        #Update and return an existing `Snippet` instance, given the validated data.
        
        instance.titulo = validated_data.get('title', instance.titulo)
        instance.code = validated_data.get('code', instance.code)
        instance.es_valido = validated_data.get('linenos', instance.es_valido)
        instance.save()
        return instance
"""

#Esto es con ModelSerializer que seria como ModelForm
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'titulo', 'code', 'es_valido']

#Esto es con ModelSerializer que seria como ModelForm
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'