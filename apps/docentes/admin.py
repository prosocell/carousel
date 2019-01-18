from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import docente

@admin.register(docente)
class Admin(ImportExportModelAdmin):
	pass