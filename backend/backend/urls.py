print("ESTOY USANDO ESTE URLS")
from django.contrib import admin
from django.urls import path
from tienda.views import home, panel, login_panel,logout_panel,eliminar_producto


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('panel/', panel, name='panel'), 
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('login/', login_panel, name='login_panel'), 
    path('logout/', logout_panel, name='logout_panel'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


