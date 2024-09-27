from rest_framework import serializers
from .models import Producto, Pedido
# Serializador para el producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'categoria', 'añodesarrollo', 'desarrollador', 'editor', 'restriccion', 'imagen']

# Serializador para el modelo Pedido
class PedidoSerializer(serializers.ModelSerializer):
    # El campo "producto" espera el ID del producto, el campo "usuario" es de solo lectura
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    usuario = serializers.StringRelatedField(read_only=True)  # Solo lectura, representado como string

    class Meta:
        model = Pedido
        fields = ['id', 'producto', 'cantidad', 'fecha', 'usuario']  # Campos a incluir en el serializador
        read_only_fields = ['usuario', 'fecha']  # El usuario y la fecha no se pueden asignar manualmente

    # Sobrescribimos el método create para asignar automáticamente el usuario autenticado
    def create(self, validated_data):
        # Asignamos el usuario autenticado al pedido
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)
