from django.shortcuts import render


from django.http import HttpResponse

from miedu.models import Bibliotecario,RegistroLibros,Prestamista
from rest_framework import viewsets
from miedu.serializers import BibliotecarioSerializer,RegistroLibrosSerializer,PrestamistaSerializer

class BibliotecarioViewSet(viewsets.ModelViewSet):
    queryset=Bibliotecario.objects.all().order_by('nombre')
    serializer_class=BibliotecarioSerializer

class RegistroLibrosViewSet(viewsets.ModelViewSet):
    queryset=RegistroLibros.objects.all().order_by('id_Libro')
    serializer_class=RegistroLibrosSerializer
class PrestamistaViewSet(viewsets.ModelViewSet):
    queryset=Prestamista.objects.all().order_by('cedula')
    serializer_class=PrestamistaSerializer

def index(request):
    return HttpResponse("Mis libros para estudiar.")