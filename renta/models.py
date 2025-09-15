from django.db import models

class Casa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    habitaciones = models.IntegerField(max_length=10,default=1)
    precio = models.FloatField(default=0)
    

class Inquilino(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.inquilino.nombre} - {self.monto}"
