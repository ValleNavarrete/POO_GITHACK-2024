# productos/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto de ropa
    descripcion = models.TextField()           # Descripción del producto
    precio = models.DecimalField(max_digits=8, decimal_places=2)  # Precio del producto
    imagen = models.ImageField(upload_to='productos/')  # Imagen del producto

    def __str__(self):
        return self.nombre

