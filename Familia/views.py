from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Buenas... es la página de mi familia.")

def probando_templates(request):
    return render(request, "template1.html", context = {})