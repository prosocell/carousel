from django.contrib import admin
from .models import comunicadosalu, comunicadosdoc, comunicadosvesp, comunicadoescolar, carusel
# Register your models here.
admin.site.register(comunicadosalu)
admin.site.register(comunicadosdoc)
admin.site.register(comunicadosvesp)
admin.site.register(comunicadoescolar)
admin.site.register(carusel)