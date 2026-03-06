from django.contrib import admin
from .models import Producto,Configuracion

admin.site.register(Producto)

config = Configuracion.objects.first()
if not config:
    config = Configuracion.objects.create(
        nombre_tienda="Mi Tienda",
        whatsapp="5490000000000"
    )