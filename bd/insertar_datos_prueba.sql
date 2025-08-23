-- ===================================
-- INSERTS DE PRUEBA PARA configurador_alfa
-- ===================================

-- 1. CLIENTES
INSERT INTO clientes (razon_social, rfc, nombre, codigo_postal, direccion, numero_telefono, correo, destino)
VALUES
('Maderas del Norte S.A. de C.V.', 'MNO123456AB1', 'Juan Pérez', '64000', 'Av. Reforma 123', '8112345678', 'ventas@maderasnorte.com', 'Monterrey, NL'),
('Industrial Pallets S.A.', 'IPS987654CD2', 'María López', '50000', 'Calle Industria 45', '7223456789', 'contacto@pallets.com', 'Toluca, Edo. Méx.');

-- 2, COSTOS
INSERT INTO costos (tipo_madera, costo)
VALUES
('Pino', 16.50),
('Oyamel', 14.50),
('Híbrido', 10.00),
('Reciclado', 7.50);

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
INSERT INTO productos (tipo, subtipo, acomodo, precio_unit, largo_gral, ancho_gral, grosor_gral)
VALUES
('Nueva',   'Barrote',   'Tradicional', 0.00, 48.00, 40.00, 5.00),
('Reciclada', 'Tacón',   'Tradicional', 0.00, 48.00, 40.00, 5.00);

-- 5. RELACIÓN PRODUCTO_SERVICIOS
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

-- 6. COMPONENTES (TS, TI, B, TAL, TAC, TC por producto)
INSERT INTO componentes (id_producto, tipo, cantidad, largo, ancho, grosor, tolerancia, separacion_TS, tipo_B, distancia_B, id_costo)
VALUES
(1,  'TS', 8, 40.00, 3.50, 0.62, '+-1/4"', 2.86,        NULL, NULL, 1),
(1,  'TI', 3, 40.00, 3.50, 0.62, '+-1/4"', NULL,        NULL, NULL, 1),
(1,   'B', 3, 48.00, 3.50, 0.62, '+-1/8"', NULL, 'Con saque', 6.00, 1),
(2,  'TS', 7, 40.00, 3.50, 0.62, '+-1/4"', 3.92,        NULL, NULL, 4),
(2,  'TI', 2, 40.00, 3.50, 0.62, '+-1/4"', NULL,        NULL, NULL, 4),
(2,  'TI', 3, 41.00, 3.50, 0.62, '+-1/4"', NULL,        NULL, NULL, 4),
(2, 'TAL', 6,  3.50, 3.50, 3.00, '+-1/8"', NULL,        NULL, NULL, 4),
(2, 'TAC', 3,  3.50, 3.50, 3.00, '+-1/8"', NULL,        NULL, NULL, 4),
(2,  'TC', 3, 48.00, 3.50, 0.62, '+-1/8"', NULL,        NULL, NULL, 4);

-- 8. ÓRDENES
INSERT INTO ordenes (id_cliente, total_estimado)
VALUES
(1, 0.00),
(2, 0.00);

-- 9. ORDEN_PRODUCTOS
INSERT INTO orden_productos (id_orden, id_producto, cantidad)
VALUES
(1, 1, 10),
(1, 2, 5),
(2, 2, 5);

-- SHOW TABLES;