# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path,include
from apps.vida.views import prog,hora,beca,noti,band,basq,danz,dib,escol,fut,haw,mari,taek,tochi,vocl,vole

urlpatterns = [
	path('programa/', prog, name="programa"),
	path('horarios/', hora, name="horarios"),
	path('beca/', beca, name="beca"),
	path('noticia/', noti, name="noticia"),
	path('banda/', band, name="band"),
	path('basquetbol/', basq, name="basq"),
	path('danza/', danz, name="danz"),
	path('dibujo/', dib, name="dib"),
	path('escolta/', escol, name="escol"),
	path('futbol/', fut, name="fut"),
	path('hawaiano/', haw, name="haw"),
	path('marimba/', mari, name="mari"),
	path('taekwondo/', taek, name="taek"),
	path('tochito/', tochi, name="tochi"),
	path('vocal y canto/', vocl, name="vocl"),
	path('voleibol/', vole, name="vole"),
	

]