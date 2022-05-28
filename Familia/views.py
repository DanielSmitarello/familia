import time
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    contex = {
        "date": datetime.now(),
    }
    return render(request, "index.html", context = contex)
