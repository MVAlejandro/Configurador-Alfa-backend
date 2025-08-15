-- ===================================
-- INSERTS DE PRUEBA PARA configurador_alfa
-- ===================================

-- 1. CLIENTES
INSERT INTO clientes (razon_social, rfc, nombre, codigo_postal, direccion, numero_telefono, correo, destino)
VALUES
('Maderas del Norte S.A. de C.V.', 'MNO123456AB1', 'Juan Pérez', '64000', 'Av. Reforma 123', '8112345678', 'ventas@maderasnorte.com', 'Monterrey, NL'),
('Industrial Pallets S.A.', 'IPS987654CD2', 'María López', '50000', 'Calle Industria 45', '7223456789', 'contacto@pallets.com', 'Toluca, Edo. Méx.');

-- 2, MATERIALES
INSERT INTO materiales (nombre, tipo_material, largo, ancho, grosor, material, unidad, costo)
VALUES
('Tabla 40x3.5 in',    'Tabla',   40.00, 3.50, 1.00, 'Pino', 'pieza', 5.00),
('Tabla 40x4 in',      'Tabla',   40.00, 4.00, 1.00, 'Pino', 'pieza', 6.50),
('Barrote 48x3.5 in',  'Barrote', 48.00, 3.50, 1.50, 'Pino', 'pieza', 8.00),
('Tacón 3.5x3.5 in',   'Tacón',    3.50, 3.50, 3.50, 'Pino', 'pieza', 4.75),
('Tabla 48x3.5 in',    'Tabla',   48.00, 3.50, 1.00, 'Pino', 'pieza', 7.50);

-- 3. SERVICIOS
INSERT INTO servicios (nombre, costo)
VALUES
('Reparado',   12.00),
('Armado',     15.00),
('HT',         18.00),
('Pintura',    10.00),
('Fumigacion',  9.00),
('Transporte', 20.00);

-- 4. PRODUCTOS
INSERT INTO productos (tipo, subtipo, acomodo, precio_unit, largo_gral, ancho_gral, grosor_gral, img_plano)
VALUES
('Nueva',     'Barrote', 'Tradicional', 0.00, 48.00, 40.00, 5.00, 'img1.png'),
('Reciclada', 'Tacón',   'Invertido',   0.00, 40.00, 48.00, 5.50, 'img2.png');

-- 5) RELACIÓN PRODUCTO_SERVICIOS
-- Producto 1: Armado, Fumigación (sin pintura), Transporte
-- Producto 2: Armado, HT, Pintura (Azul), Transporte
INSERT INTO producto_servicios (id_producto, id_servicio, color)
VALUES
(1, 2, NULL),      -- Armado
(1, 5, NULL),      -- Fumigación
(1, 6, NULL),      -- Transporte
(2, 1, NULL),      -- Reparación
(2, 2, NULL),      -- Armado
(2, 3, NULL),      -- HT
(2, 4, 'Azul'),    -- Pintura con color
(2, 6, NULL);      -- Transporte

-- 6. PARRILLAS (TS, TI, TC por producto)
INSERT INTO parrillas (id_producto, tipo, tolerancias)
VALUES
(1, 'TS', '+-1/4"'),
(1, 'TI', '+-1/4"'),
(1, 'TC', '+-1/8"'),
(2, 'TS', '+-1/4"'),
(2, 'TI', '+-1/4"'),
(2, 'TC', '+-1/8"');

-- 7. PARRILLA_MATERIALES
INSERT INTO parrilla_materiales (id_parrilla, id_material, cantidad)
VALUES
-- Producto 1 - TS
(1, 1, 8),
-- Producto 1 - TI
(2, 1, 3),
-- Producto 1 - TC
(3, 3, 3),
-- Producto 2 - TS
(4, 1, 7),
-- Producto 2 - TI
(5, 1, 2),
(5, 2, 3),
-- Producto 2 - TC
(6, 4, 9),
(6, 5, 3);

-- 8. ÓRDENES
INSERT INTO ordenes (id_cliente, total_estimado)
VALUES
(1, 0.00),
(2, 0.00);

-- 9 ORDEN_PRODUCTOS
INSERT INTO orden_productos (id_orden, id_producto, cantidad)
VALUES
(1, 1, 10),
(1, 2, 5),
(2, 2, 5);

-- SHOW TABLES;