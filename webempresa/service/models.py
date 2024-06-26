from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    subtitle = models.CharField(max_length=200,verbose_name="Subtítulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #auto_now_add=True captura el valor y lo guarda, solo en la creacion
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización") # captura el valor y lo guarda en cada actualizacion

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title