from django.contrib import admin


# Register your models here.
from .models import Bibliotecario
from .models import RegistroLibros
from .models import Prestamista

admin.site.register(Bibliotecario)
admin.site.register(RegistroLibros)
admin.site.register(Prestamista)
