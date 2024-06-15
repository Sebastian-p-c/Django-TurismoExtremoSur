from django.db import models

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='services_photos/')
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion
