from django.contrib import admin
from .models import Producto, Configuracion

admin.site.register(Producto)
admin.site.register(Configuracion) # Regístralo normal para poder editarlo