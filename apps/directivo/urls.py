from __future__ import unicode_literals,absolute_import
from django.urls import path,include, re_path
from apps.directivo.views import comunicadoalu, comunicadodoc, directivo, comunicadovesp, comunicadosescolar, excel, subirimage, borrar_imagen

urlpatterns = [
	#path('',index),
    path('directivo/',directivo, name="directivo" ),
    path('comalu/', comunicadoalu, name="comalu"),   
    path('comdoc/', comunicadodoc, name="comdoc"),
    path('comvesp/',comunicadovesp, name="comvesp"),
    path('comuesco/',comunicadosescolar, name="comuesco"),
    path('excel/', excel, name="excel"),
    path('subirimage/', subirimage, name="subirimage"),
    re_path('borrarimagen/(?P<id>\d+)/', borrar_imagen),




]