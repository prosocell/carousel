from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.

class carusel(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Titulo")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "carousel")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de edicion")

    class Meta:
        verbose_name = "carusel"
        verbose_name_plural = "carusell"
        ordering = ["-created"]
    def __str__(self):
        return self.title
            
class comunicadosalu(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripcion")
    archivo = models.FileField(verbose_name = "Archivo", blank=True, null=True, upload_to="comalu")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edicion")

    class Meta: 
        verbose_name = "Comunicados Alumnos"
        verbose_name_plural = "Comunicados Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class comunicadosvesp(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripcion")
    archivo = models.FileField(verbose_name = "Archivo", blank=True, null=True, upload_to="comalu")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edicion")

    class Meta: 
        verbose_name = "Comunicados Docentes"
        verbose_name_plural = "Comunicados Docentes vesp"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class comunicadosdoc(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripcion")
    archivo = models.FileField(verbose_name = "Archivo", blank=True, null=True, upload_to="comalu")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edicion")

    class Meta: 
        verbose_name = "Comunicados Docentes"
        verbose_name_plural = "Comunicados Docentes"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class comunicadoescolar(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="comalu")
    U_TURNO = (('Di','Dibujo'),('Ta','Taekwondo'),('Ha','Hawaiano'),('Da','Danza'),('Ma','Marimba'),('Vc','Vocalizacionycanto'),('Ba','Bandadeguerra'),('To','Tochito'),('Es','Escolta'),('Bas','Basquetbol'),('Fu','Futbol'),('Vo','Voleibol'))
    categoria = models.CharField(max_length=2,blank=True,null=True,choices=U_TURNO)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "comunicado escolar"
        verbose_name_plural = "comunicados escolar"
        ordering = ["-created"]

    def __str__(self):
        return self.title        

class horarios(models.Model):
    #nombre = models.CharField(max_length=30, verbose_name = "doch")
    U_GRADO = (('1','Primero'),('2','Segundo'),('3','Tercero'),('4','Cuarto'),('5','Quinto'),('6','Sexto'))
    grado =models.CharField(max_length=2,blank=True, verbose_name = "Grado",null=True, choices=U_GRADO)
    U_GRUPO = (('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('I','I'))
    grupo = models.CharField(max_length=2,blank=True,null=True, verbose_name = "Grupo", choices=U_GRUPO)
    capacitacion = models.CharField( max_length=20, blank=True, verbose_name = "capacitacion")
    U_TURNO = (('Ma','Matutino'),('Ve','Vespertino'),)
    turno = models.CharField(max_length=2,blank=True,null=True,choices=U_TURNO)
    periodolec = models.CharField( max_length=20, blank=True, verbose_name = "capacitacion")
    asignatura = models.CharField( max_length=20, blank=True, verbose_name = "asignatura")
    lunes = models.CharField( max_length=10, blank=True, verbose_name = "lunes")
    martes = models.CharField( max_length=10, blank=True, verbose_name = "martes")
    miercoles = models.CharField( max_length=10, blank=True, verbose_name = "miercoles")
    jueves = models.CharField( max_length=10, blank=True, verbose_name = "jueves")
    vierne = models.CharField( max_length=10, blank=True, verbose_name = "viernes")
    aula = models.CharField( max_length=10, blank=True, verbose_name = "aulas")
    docente = models.CharField( max_length=40, blank=True, verbose_name = "docente")

    def __str__(self):
        return self.turno


    
  