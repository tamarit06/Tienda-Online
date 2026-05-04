from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_config(sender, **kwargs):
    # Esto solo se ejecutará DESPUÉS de que las migraciones hayan terminado
    from .models import Configuracion
    if not Configuracion.objects.exists():
        Configuracion.objects.create(
            nombre_tienda="Mi Tienda",
            whatsapp="5490000000000"
        )

class TiendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tienda' 

    def ready(self):
        # Conectamos la función al final de la migración
        post_migrate.connect(create_default_config, sender=self)