from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=150)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    numero_telefono = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    destino = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Costos(models.Model):
    id_costo = models.AutoField(primary_key=True)
    tipo_madera = models.CharField(max_length=50, blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'costos'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    subtipo = models.CharField(max_length=50, blank=True, null=True)
    acomodo = models.CharField(max_length=50, blank=True, null=True)
    precio_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    largo_gral = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ancho_gral = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    grosor_gral = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Componentes(models.Model):
    id_componente = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    tipo = models.CharField(max_length=20)  # 'TS', 'TI', 'B', 'TA', 'TC'
    cantidad = models.IntegerField()
    largo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ancho = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    grosor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tolerancia = models.CharField(max_length=100, blank=True, null=True)
    separacion_TS = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo_B = models.CharField(max_length=50, blank=True, null=True)
    distancia_B = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_costo = models.ForeignKey(Costos, models.DO_NOTHING, db_column='id_costo')

    class Meta:
        managed = False
        db_table = 'componentes'

class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'servicios'


class ProductoServicios(models.Model):
    id_producto_servicio = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    id_servicio = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='id_servicio')
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_servicios'


class Ordenes(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        managed = False
        db_table = 'ordenes'


class OrdenProductos(models.Model):
    id_orden_producto = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_orden')
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_productos'