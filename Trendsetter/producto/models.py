from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    descripcion = models.TextField() 
    Unidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Create your models here.
