import time
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f"Hoy es {fecha} !!"
    return HttpResponse(mensaje)


def index(request):
    contex = {
        "date": datetime.now(),  # es una prueba para visualizar la fecha en un html
    }
    return render(request, 'index.html',context = contex)
