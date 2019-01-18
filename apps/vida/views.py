from django.shortcuts import render, HttpResponse
from apps.directivo.models import comunicadoescolar
# Create your views here.
def prog(request):
	return render(request, "vida/programa.html")

def hora(request):
	return render(request, "vida/horarios.html")

def beca(request):
	return render(request, "vida/becas.html")

def noti(request):
	return render(request, "vida/noticia.html")
	#TODOS LOS COMUNICADOS
	#class Comunicado_list(ListView):
  #  model = comunicadoescolar
    
  #  def get(self, request, *args,**kwargs):
        #turno = request.user.turno
        #print(turno)
   #     comunicado = comunicadoescolar.objects.filter(categoria=Fu)
        #print(comunicado)
    
   #     return render(request, "comunicadoescolar/comunicadoescolar.html", {'comunicado':comunicado})
def band(request):
	projects = comunicadoescolar.objects.filter(categoria=Ba)
	return render(request, "vida/band.html",{'projects': projects })

def basq(request):
	projects1 = comunicadoescolar.objects.filter(categoria=Bas)
	return render(request, "vida/basq.html",{'projects1': projects1 })

def danz(request):
	projects2 = comunicadoescolar.objects.filter(categoria=Da)
	return render(request, "vida/danz.html",{'projects2': projects2 })

def dib(request):
	#projects3 = comunicadoescolar.objects.all()
	projects3 = comunicadoescolar.objects.filter(categoria=Di)
	return render(request, "vida/dib.html",{'projects3': projects3 })

def escol(request):
	projects4 = comunicadoescolar.objects.filter(categoria=Es)
	return render(request, "vida/escol.html",{'projects4': projects4 })

def fut(request):
	projects5 = comunicadoescolar.objects.filter(categoria=Fu)
	return render(request, "vida/fut.html",{'projects5': projects5 })

def haw(request):
	projects6 = comunicadoescolar.objects.filter(categoria=Ha)
	return render(request, "vida/haw.html",{'projects6': projects6 })

def mari(request):
	projects7 = comunicadoescolar.objects.filter(categoria=Ma)
	return render(request, "vida/mari.html",{'projects7': projects7 })

def taek(request):
	projects8 = comunicadoescolar.objects.filter(categoria=Ta)
	return render(request, "vida/taek.html",{'projects8': projects8 })

def tochi(request):
	projects9 = comunicadoescolar.objects.filter(categoria=To)
	return render(request, "vida/tochi.html",{'projects9': projects9 })

def vocl(request):
	projects10 = comunicadoescolar.objects.filter(categoria=Vc)
	return render(request, "vida/vocl.html",{'projects10': projects10 })

def vole(request):
	projects11 = comunicadoescolar.objects.filter(categoria=Vo)
	return render(request, "vida/vole.html",{'projects11': projects11 })
