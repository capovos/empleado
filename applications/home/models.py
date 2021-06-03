from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos de prueba'
        ordering = ['-titulo']
    
    def __str__(self):
        return self.titulo