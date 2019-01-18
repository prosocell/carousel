# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from apps.inicio.views import login, contact, quinsom, prop, orga, mivi, valo, equidir, calen, index


urlpatterns = [
    #path('',LoginView.as_view(template_name='index.html'), name='inicio'),
    path('',index),
    path('login/', login, name="login"),
    path('contact/',contact, name="contact"), 
    path('quinsom/', quinsom, name="quinsom"),
    path('proposito/', prop, name="proposito"),
    path('organigrama/',orga, name="organigrama"),
    path('mivi/', mivi, name="mivi"),
    path('valores/', valo, name="valores"),
    path('equidir/', equidir, name="equidir"),
    path('calendario/', calen, name="calendario"),
   
]
