from django.shortcuts import render,redirect
from .models import Producto,Configuracion
from .forms import ProductoForm, ConfiguracionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def home(request):
    productos = Producto.objects.all()
    config = Configuracion.objects.last()  # modelo que guarda el WhatsApp

    return render(request, 'index.html', {
        'productos': productos,
        'config': config
    })


@login_required
def panel(request):

    # Ver si se está editando un producto
    producto_id = request.GET.get('editar')
    producto = get_object_or_404(Producto, id=producto_id) if producto_id else None

    # Configuración actual
    config = Configuracion.objects.last()

    # Formularios iniciales (esto evita el error)
    form = ProductoForm(instance=producto) if producto else ProductoForm()
    config_form = ConfiguracionForm(instance=config) if config else ConfiguracionForm()

    if request.method == 'POST':

        # GUARDAR PRODUCTO
        if 'guardar_producto' in request.POST:

            if producto:
                form = ProductoForm(request.POST, request.FILES, instance=producto)
            else:
                form = ProductoForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('panel')

        # GUARDAR CONFIG
        elif 'guardar_config' in request.POST:

            if not config:
                config = Configuracion.objects.create(nombre_tienda="", whatsapp="")

            config_form = ConfiguracionForm(request.POST, instance=config)

            if config_form.is_valid():
                config_form.save()
                return redirect('panel')

    productos = Producto.objects.all()

    return render(request, 'panel.html', {
        'form': form,
        'productos': productos,
        'editando': producto,
        'config_form': config_form
    })
@login_required
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('panel')

def login_panel(request):
    from .forms import LoginForm
    mensaje = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel')
            else:
                mensaje = "Usuario o contraseña incorrectos"
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form, 'mensaje': mensaje})
def logout_panel(request):
    logout(request)
    return redirect('login_panel')

