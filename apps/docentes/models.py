from django.db import models

# Create your models here.


class docente(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	email = models.EmailField()
	sexo = models.CharField(max_length=10)
	edad = models.IntegerField()
	fecha = models.DateField()


	def __str__(self):
		return self.nombre