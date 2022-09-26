from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ingreseNombre(request):
    nom="<h1>HOLA CTM</h1><label>Ingrese nombre:</label><br><input></input>"
    return HttpResponse(nom)

def saludito(request):
    par="<p>asdjkhasfjkfhasbfjadnjkfgb asjbfasdbhfasbf</p>"
    return HttpResponse(par)
