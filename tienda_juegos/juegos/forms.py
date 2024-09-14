# juegos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'categoria', 'añodesarrollo', 'desarrollador', 'editor', 'restriccion']
