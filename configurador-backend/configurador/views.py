from django.shortcuts import render

from rest_framework import viewsets
from .models import (
    Clientes, Materiales, OrdenProductos, Ordenes,
    ParrillaMateriales, Parrillas, ProductoServicios,
    Productos, Servicios
)
from .serializers import (
    ClientesSerializer, MaterialesSerializer, OrdenProductosSerializer, OrdenesSerializer,
    ParrillaMaterialesSerializer, ParrillasSerializer, ProductoServiciosSerializer,
    ProductosSerializer, ServiciosSerializer
)

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

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