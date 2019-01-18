from import_export import resources
from docentes.models import docente

class Resource(resources.ModelResource):
    class Meta:
    	model = docente   

