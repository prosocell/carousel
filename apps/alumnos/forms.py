from django import forms
from .models import alumno

class excelalu(forms.ModelForm):

	class Meta:
		model = alumno
		fields = ('matricula','clacentro','nombreplan',) 