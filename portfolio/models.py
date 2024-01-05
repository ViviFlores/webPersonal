from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    description=models.TextField(verbose_name="Descripción")
    image=models.ImageField(upload_to="portfolio", verbose_name="Imagen")
    url=models.URLField(null=True, blank=True, verbose_name="Enlace")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']
    
    def __str__(self):
        return self.title