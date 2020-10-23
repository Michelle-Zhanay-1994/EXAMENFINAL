from django.db import models


class Bibliotecario(models.Model):
    nombre = models.CharField(max_length=50,default="N/A")
    cedula = models.IntegerField(default=10)
    direccion = models.CharField(max_length=50,default="N/A")
    telefono = models.IntegerField(default=10)
   

class RegistroLibros(models.Model):
    id_Libro=models.IntegerField(default=5)
    nombre_Libros=models.CharField(max_length=100,default="N/A")
    numero_paginas=models.IntegerField(default=5)
    autor=models.CharField(max_length=50,default="N/A")
    nivel_academico=models.CharField(max_length=50,default="N/A")
  
    
class Prestamista(models.Model):
    nombre = models.CharField(max_length=50,default="N/A")
    cedula = models.IntegerField(default=10)
    direccion = models.CharField(max_length=50,default="N/A")
    telefono = models.IntegerField(default=10)
    curso = models.CharField(max_length=20,default="N/A")