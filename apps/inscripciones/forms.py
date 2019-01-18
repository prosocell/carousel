from django import forms

class contac(forms.Form):
	name = forms.CharField(label="nombre", required=True)
	apellido = forms.CharField(label="apellido",required=True)
	content = forms.CharField(label="content",required=True)
		