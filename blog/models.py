from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return f"({self.apellido}) {self.nombre}"


class Libro(models.Model):
    class Meta:
        verbose_name_plural = "Libros"

    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    publicacion = models.DateField(null=True)

    def __str__(self):
        return f"{self.titulo}, {self.genero}, {self.publicacion}"


class Editorial(models.Model):
    class Meta:
        verbose_name_plural = "Editorial"

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)