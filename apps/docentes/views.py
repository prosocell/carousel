from django.shortcuts import render
from .models import docente

# Create your views here.
def docentes(request):
    projects = docente.objects.all()
    return render(request,"docentes/docentes.html", {'projects':projects})

def infdoc(request):
    projects = docente.objects.all()
    return render(request, "docentes/infdoc.html", {'projects':projects})


