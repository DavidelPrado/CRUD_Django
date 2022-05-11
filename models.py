from django.db import models

# Create your models here.

class Usuario(models.Model):
    DNI = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=100)
    fechaNac = models.DateField(null=True, blank=True)
