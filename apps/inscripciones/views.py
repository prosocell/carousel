from django.shortcuts import render, HttpResponse
from django.conf import settings
from .forms import contac
import reportlab
# Create your views here.
#def inscripcion(request):
#	return render(request,'inscripciones/inscrip.html')


def forma(request):
	return render(request, "inscripciones/formato.html")

def pag(request):
	return render(request, "inscripciones/pago.html")

def convo(request):
	return render(request, "inscripciones/convocatoria.html")

def nuevo(request):
	
	return render(request, "inscripciones/nuevo.html")

def cursador(request):
	return render(request, "inscripciones/cursadores.html")
	
def normal(request):
	return render(request, "inscripciones/normal.html")

def repite(request):
	return render(request, "inscripciones/repetidor.html")
