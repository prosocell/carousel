# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path,include
from apps.docentes.views import docentes
from apps.docentes.views import infdoc



urlpatterns = [

    path('docentes/',docentes, name="docentes"),
    path('infdoc/',infdoc, name="infdoc"),

]
 