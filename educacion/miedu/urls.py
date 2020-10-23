from django.urls import path
from . import views

from django.conf.urls import include,url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Bibliotecario',views.BibliotecarioViewSet)
router.register(r'RegistroLibros',views.RegistroLibrosViewSet)
router.register(r'Prestamista',views.PrestamistaViewSet)

urlpatterns = [
    path('',views.index, name='index'),
    url(r'^',include(router.urls)),
    url(r'^api-auth',include('rest_framework.urls',namespace='rest_framework'))
]
