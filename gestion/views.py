from django.shortcuts import render
from api.serializers import SnippetSerializer

# Create your views here.

def Pedidos(request):
    print("Entramos aqui")
    contexto={'prueba':'jaramillo'}
    return render(request,"gestion/gestion1.html",contexto)
