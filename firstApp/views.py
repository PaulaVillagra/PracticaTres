from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>Hola mundo</h1>")

def displayDateTime (request):
    dt=datetime.datetime.now()
    s="<b>La fecha y hora actual son: </b>"+str(dt)
    return HttpResponse(s)