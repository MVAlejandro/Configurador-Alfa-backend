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