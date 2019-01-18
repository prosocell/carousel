from __future__ import unicode_literals, absolute_import
from django.urls import path,include
from apps.alumnos.views import alumnos, kardex, infalu, boleta

urlpatterns = [
	path('alumnos/', alumnos, name="alumnos"),
	path('kardex/', kardex, name="kardex"),
	path('infalu/', infalu, name="infalu"),
	path('boleta/', boleta, name="boleta"),
	
	]