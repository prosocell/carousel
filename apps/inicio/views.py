from django.shortcuts import render, HttpResponse
from .models import *
from apps.directivo.models import *


# Create your views here.
def contact(request):
    return render(request, "contact/contact.html")
	

#vistas pestaña 1
def quinsom(request):
	return render(request, "quinsom/quinsom.html")

def prop(request):
	return render(request, "quinsom/proposito.html")

def orga(request):
	return render(request, "quinsom/organigrama.html")

def mivi(request):
	return render(request, "quinsom/vimi.html")

def valo(request):
	return render(request, "quinsom/valores.html")

def equidir(request):
	return render(request, "quinsom/equidir.html")

def calen(request):
	return render(request, "quinsom/calendario.html")

#vista logeo
def login(request):
	return render(request, "inicio/login.html")

def index(request):
	slider = carusel.objects.all()
	return render(request, "index.html",{"slider":slider})

