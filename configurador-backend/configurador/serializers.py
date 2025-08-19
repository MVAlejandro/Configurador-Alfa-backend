from rest_framework import serializers
from .models import (
    Clientes, Materiales, OrdenProductos, Ordenes,
    ParrillaMateriales, Parrillas, ProductoServicios,
    Productos, Servicios
)

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class MaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        fields = '__all__'

class OrdenProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProductos
        fields = '__all__'

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = '__all__'

class ParrillaMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParrillaMateriales
        fields = '__all__'

class ParrillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parrillas
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

class MaterialDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        fields = ['id_material', 'nombre', 'tipo', 'largo', 'ancho', 'grosor', 'unidad', 'costo']

class ParrillaMaterialDetalleSerializer(serializers.ModelSerializer):
    material = MaterialDetalleSerializer(source='id_material')

    class Meta:
        model = ParrillaMateriales
        fields = ['id_parrilla_material', 'cantidad', 'material']

class ParrillaDetalleSerializer(serializers.ModelSerializer):
    materiales = ParrillaMaterialDetalleSerializer(source='parrillamateriales_set', many=True)

    class Meta:
        model = Parrillas
        fields = ['id_parrilla', 'tipo', 'tolerancias', 'extra', 'extra_2', 'materiales']

class ProductoServicioDetalleSerializer(serializers.ModelSerializer):
    servicio = serializers.CharField(source='id_servicio.nombre') 

    class Meta:
        model = ProductoServicios
        fields = ['id_producto_servicio', 'color', 'servicio']

class ProductoDetalleSerializer(serializers.ModelSerializer):
    parrillas = ParrillaDetalleSerializer(source='parrillas_set', many=True)
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
            'img_plano',
            'parrillas',
            'servicios'
        ]