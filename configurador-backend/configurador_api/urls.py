"""
URL configuration for configurador_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from configurador.views import (
    ClientesViewSet, MaterialesViewSet, OrdenProductosViewSet, OrdenesViewSet,
    ParrillaMaterialesViewSet, ParrillasViewSet, ProductoServiciosViewSet,
    ProductosViewSet, ServiciosViewSet
)

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'materiales', MaterialesViewSet)
router.register(r'orden_productos', OrdenProductosViewSet)
router.register(r'ordenes', OrdenesViewSet)
router.register(r'parrilla_materiales', ParrillaMaterialesViewSet)
router.register(r'parrillas', ParrillasViewSet)
router.register(r'producto_servicios', ProductoServiciosViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'servicios', ServiciosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]