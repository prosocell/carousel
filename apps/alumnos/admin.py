from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import alumno, calificacion
# Register your models here.
@admin.register(alumno)
class Admin(ImportExportModelAdmin):
	pass
@admin.register(calificacion)
class Admin(ImportExportModelAdmin):
	pass

	#class calificacionResource(resources.ModelResource):
	#class Meta:
	#model = calificacion
	#fields = ('clacentro','claveplan','nombreplan','clavemate','materia','semestre','clavegrupo','turno','matricula','parcial_1','parcial_2','parcial_3','calificaci','prompar','promsem','inasistenc','numclases','inasispar1','nclasespar','inasispar2','nclasespa2','inasispar3','nclasespa3','edoacredit','grado','grupo','orden')


