from django.db import models

class Datosbanesco(models.Model):
    nombre = models.CharField(max_length=100) 
    fecha_up = models.DateField('fecha de subida')
    archivo = models.FileField(upload_to='banescofiles')

    def __str__(self):
        return self.nombre

# Create your models here.

