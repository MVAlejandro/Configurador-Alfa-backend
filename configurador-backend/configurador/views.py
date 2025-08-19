from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Clientes, Materiales, OrdenProductos, Ordenes,
    ParrillaMateriales, Parrillas, ProductoServicios,
    Productos, Servicios
)
from .serializers import (
    ClientesSerializer, MaterialesSerializer, OrdenProductosSerializer, OrdenesSerializer,
    ParrillaMaterialesSerializer, ParrillasSerializer, ProductoServiciosSerializer,
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

class MaterialesViewSet(viewsets.ModelViewSet):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializer

class OrdenProductosViewSet(viewsets.ModelViewSet):
    queryset = OrdenProductos.objects.all()
    serializer_class = OrdenProductosSerializer

class OrdenesViewSet(viewsets.ModelViewSet):
    queryset = Ordenes.objects.all()
    serializer_class = OrdenesSerializer

class ParrillaMaterialesViewSet(viewsets.ModelViewSet):
    queryset = ParrillaMateriales.objects.all()
    serializer_class = ParrillaMaterialesSerializer

class ParrillasViewSet(viewsets.ModelViewSet):
    queryset = Parrillas.objects.all()
    serializer_class = ParrillasSerializer

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