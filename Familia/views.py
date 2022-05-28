import time
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f"Hoy es {fecha} !!"
    return HttpResponse(mensaje)


def saludo(request):
    return HttpResponse("Buenas... es la página de mi familia.")

def probando_templates(request):
    contex = {
        "date": datetime.now(),
    }
    return render(request, "template1.html", context = contex)