from import_export import resources
from alumnos.models import alumno, calificacion

class Resource(resources.ModelResource):
    class Meta:
    	model = alumno
    	model = calificacion    

