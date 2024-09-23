from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'categoria', 'añodesarrollo', 'desarrollador', 'editor', 'restriccion', 'imagen']
