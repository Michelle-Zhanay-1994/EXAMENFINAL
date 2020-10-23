from miedu.models import Bibliotecario,RegistroLibros,Prestamista
from rest_framework import serializers

class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bibliotecario
        fields = ('nombre' , 'cedula' , 'direccion' , 'telefono')

class RegistroLibrosSerializer(serializers.ModelSerializer):    
    class Meta:
        model=RegistroLibros
        fields=('id_Libro' , 'nombre_Libros' , 'numero_paginas' , 'autor','nivel_academico')
class PrestamistaSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Prestamista
        fields=('nombre' , 'cedula' , 'direccion' , 'telefono','curso')