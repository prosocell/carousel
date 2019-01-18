from django.shortcuts import render
from .models import comunicadosalu, comunicadosdoc, comunicadosvesp, comunicadoescolar,carusel
from .forms import subirForm, escolarForm
#def carusell(request):
#	projects4 = carusel.objects.all()
#	return render(request,"templates/index.html",{'projects4':projects4})

#def index(request):
#	slider = carusel.objects.all()
#	return render(request, "templates/index.html",{"slider":slider})

def directivo(request):
	return render(request, "directivo/director.html")

def comunicadoalu(request):
	projects = comunicadosalu.objects.all()
	return render(request,"comunicadosalu/comunicadosalu.html",{'projects': projects } )

def comunicadodoc(request):
	projects1 = comunicadosdoc.objects.all()
	return render(request,"comunicadosdoc/comunicadosdoc.html",{'projects1': projects1 } ) 

def comunicadovesp(request):
	projects2 = comunicadosvesp.objects.all()
	return render(request, "comunicadosvesp/comunicadosvesp.html", {'projects2': projects2})

def comunicadosescolar(request):
	projects3 = comunicadoescolar.objects.all()
	return render(request, "comunicadosescolar/comunicadosescolar.html", {'projects3':projects3})
	
def excel(request):
	projects4 = carusel.objects.all()
	return render(request, "directivo/excel.html",{'projects4':projects4})
 #bammer para atraer las imagenes 
def banner(request):
	slider = carusel.objects.get(id=id)
	return render(request, "index.html", {"slider":slider})
#muestra las imagenes cargadas en una vista
def image_update(request):
	images = carusel.objects.all()
	return render(request,"excel.html",{"images":images})
#borra la imagen 
def borrar_imagen(request, id):
	del_img = carusel.objects.get(id=id)
	del_img.delete()
	return render(request, "directivo/excel.html")
#boton de subir imagen de carousell
def subirimage(request):
	if request.method == 'POST':
		lol = subirForm(request.POST, request.FILES)
		if lol.is_valid():
			lol.save()
			mensaje = "imagen guardada exitosamente"
	else:
		lol = subirForm()
	return render(request, "directivo/subir.html", locals())

def subirescolar(request):
	if request.method == 'POST':
		form = escolarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			message = "categoria subida de escolar"
	else:
		form = escolarForm()
	return render(request, "directivo/subir.html")

#class Comunicado_list(ListView):
  #  model = comunicadoescolar
    
  #  def get(self,request,args,*kwars):
        #turno = request.user.turno
        #print(turno)
   #     comunicado = comunicadoescolar.objects.filter(categoria=Fu)
        #print(comunicado)
    
   #     return render(request, "comunicadoescolar/comunicadoescolar.html", {'comunicado':comunicado})