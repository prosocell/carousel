# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path,include
from apps.inscripciones.views import forma, pag, convo, nuevo, cursador, normal, repite
#inscripcion, ,  convocatoria
 



urlpatterns = [

    #path('inscripciones/', inscripcion, name="inscripciones"),
    path('formato/', forma, name="formato"),
    path('pago/', pag, name="pago"),
    path('convocatoria/', convo, name="convocatoria"),
    path('nuevo/', nuevo, name='nuevo'),
    path('cursador/', cursador, name='cursadores'),
    path('normal/', normal, name='normal'),
    path('repetidor', repite, name='repetidor'),
    
]
#018000212345 opcion 3