from django import forms
from .models import carusel, comunicadosalu, comunicadosvesp, comunicadosdoc, comunicadoescolar

class subirForm(forms.ModelForm):
	class Meta:
		model = carusel
		fields = ('image','title') 

class subircomForm(forms.ModelForm):
	class Meta:
		model = comunicadosalu
		fields = ('title','description','archivo',) 

class escolarForm(forms.ModelForm):
	class Meta:
		model = comunicadoescolar
		fields = ('title','description','image')
