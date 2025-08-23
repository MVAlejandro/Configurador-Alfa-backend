from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Clientes, Costos, OrdenProductos, 
    Ordenes, Componentes, ProductoServicios,
    Productos, Servicios
)
from .serializers import (
    ClientesSerializer, CostosSerializer, OrdenProductosSerializer, 
    OrdenesSerializer, ComponentesSerializer, ProductoServiciosSerializer,
    ProductosSerializer, ServiciosSerializer, ProductoDetalleSerializer
)

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    @action(detail=False, methods=['post'])
    def registrar_o_buscar(self, request):
        rfc = request.data.get('rfc')
        correo = request.data.get('correo')
        cliente, created = Clientes.objects.get_or_create(
            rfc=rfc,
            correo=correo,
            defaults=request.data
        )
        return Response({'id_cliente': cliente.id_cliente, 'created': created})

class CostosViewSet(viewsets.ModelViewSet):
    queryset = Costos.objects.all()
    serializer_class = CostosSerializer

class OrdenProductosViewSet(viewsets.ModelViewSet):
    queryset = OrdenProductos.objects.all()
    serializer_class = OrdenProductosSerializer

class OrdenesViewSet(viewsets.ModelViewSet):
    queryset = Ordenes.objects.all()
    serializer_class = OrdenesSerializer

class ComponentesViewSet(viewsets.ModelViewSet):
    queryset = Componentes.objects.all()
    serializer_class = ComponentesSerializer

class ProductoServiciosViewSet(viewsets.ModelViewSet):
    queryset = ProductoServicios.objects.all()
    serializer_class = ProductoServiciosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

# --- Serializadores compuestos ---
class ProductoDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoDetalleSerializer