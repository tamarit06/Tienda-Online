from django import forms
from .models import Producto, Configuracion


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']




class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['nombre_tienda', 'whatsapp']
        widgets = {
            'nombre_tienda': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
        }