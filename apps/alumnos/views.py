from django.shortcuts import render
from .models import calificacion, alumno
from .forms import excelalu

def alumnos(request):
	return render(request, "alumnos/alumnos.html")

def kardex(request):
    return render(request, "alumnos/kardex.html")
	

def infalu(request):
   projects1 = alumno.objects.all()
   return render(request, "alumnos/infalu.html", {'projects1':projects1})

def boleta(request):
	return render(request, "alumnos/boleta.html")
	#projects3 = calificacion.objects.all()
	#, {'projects3':projects3})


def actuex(request):
	if  request.method == 'POST':
		form = excelalu(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			message = "el excel se cargo exitosamente"
	else:
		form = excelalu()
	return render(request, "directorio/subir.html", locals())

def admi(request):
	return render(request, "admi/admi.html")