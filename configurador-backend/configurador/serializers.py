from rest_framework import serializers
from .models import (
    Clientes, Costos, OrdenProductos, 
    Ordenes, Componentes, ProductoServicios,
    Productos, Servicios
)

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class CostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costos
        fields = '__all__'

class OrdenProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProductos
        fields = '__all__'

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = '__all__'

class ComponentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componentes
        fields = '__all__'

class ProductoServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicios
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'


# --- Serializadores compuestos ---

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costos
        fields = ['id_costo', 'tipo_madera', 'costo']

class ComponenteDetalleSerializer(serializers.ModelSerializer):
    costo = CostoSerializer(source='id_costo')

    class Meta:
        model = Componentes
        fields = [
            'id_componente', 'tipo', 'cantidad', 'largo', 'ancho', 'grosor',
            'tolerancia', 'separacion_TS', 'tipo_B', 'distancia_B', 'costo'
        ]

class ProductoServicioDetalleSerializer(serializers.ModelSerializer):
    servicio = serializers.CharField(source='id_servicio.nombre') 

    class Meta:
        model = ProductoServicios
        fields = ['id_producto_servicio', 'color', 'servicio']

class ProductoDetalleSerializer(serializers.ModelSerializer):
    componentes = ComponenteDetalleSerializer(source='componentes_set', many=True)
    servicios = ProductoServicioDetalleSerializer(source='productoservicios_set', many=True)

    class Meta:
        model = Productos
        fields = [
            'id_producto',
            'tipo',
            'subtipo',
            'acomodo',
            'precio_unit',
            'largo_gral',
            'ancho_gral',
            'grosor_gral',
            'componentes',
            'servicios'
        ]