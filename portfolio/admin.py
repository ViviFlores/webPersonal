from django.contrib import admin
from .models import Project

# Configuraciones extendidas del administrador
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# Register your models here.
admin.site.register(Project, ProjectAdmin)  # Registramos en el administrador / gestionar el modelo
