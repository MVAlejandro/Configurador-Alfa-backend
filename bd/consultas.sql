USE configurador_alfa;

SELECT * FROM clientes;
SELECT * FROM costos;
SELECT * FROM servicios;
SELECT * FROM componentes;
SELECT * FROM productos;

SELECT o.id_orden, c.razon_social, o.fecha_creacion, o.total_estimado
FROM ordenes o
JOIN clientes c ON o.id_cliente = c.id_cliente;

SELECT op.id_orden, prod.tipo, prod.subtipo, op.cantidad
FROM orden_productos op
JOIN productos prod ON op.id_producto = prod.id_producto;

-- Consulta para calcular el precio de un producto
SELECT
    p.id_producto,
    p.tipo,
    p.subtipo,
    COALESCE(ROUND(costo_componentes, 2), 0) AS costo_componentes,
    COALESCE(ROUND(costo_servicios, 2), 0) AS costo_servicios,
    COALESCE(ROUND(costo_componentes + costo_servicios, 2), 0) AS precio_unit
FROM productos p
-- Subconsulta para componentes
LEFT JOIN (
    SELECT 
        c.id_producto,
        SUM((c.largo * c.ancho * c.grosor / 144) * cos.costo * c.cantidad) AS costo_componentes
    FROM componentes c
    JOIN costos cos ON cos.id_costo = c.id_costo
    GROUP BY c.id_producto
) comp ON comp.id_producto = p.id_producto
-- Subconsulta para servicios
LEFT JOIN (
    SELECT 
        ps.id_producto,
        SUM(s.costo) AS costo_servicios
    FROM producto_servicios ps
    JOIN servicios s ON s.id_servicio = ps.id_servicio
    GROUP BY ps.id_producto
) serv ON serv.id_producto = p.id_producto;