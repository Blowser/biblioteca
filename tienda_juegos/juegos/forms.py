# juegos/forms.py
from django import forms
from .models import Producto, Pedido


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'categoria', 'añodesarrollo', 'desarrollador', 'editor', 'restriccion', 'imagen']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad']
