-- ===================================
-- INSERTS PARA configurador_alfa
-- ===================================

-- 1. CLIENTES

-- 2, COSTOS
INSERT INTO costos (tipo_madera, costo)
VALUES
('Pino', 16.50),
('Oyamel', 14.50),
('Híbrido', 12.00),
('Reciclado', 8.00);

-- 3. SERVICIOS
INSERT INTO servicios (nombre, costo)
VALUES
('Reparado',   6.72),
('Armado',     7.84),
('HT',         10.00),
('Pintura',    8.00),
('Fumigacion',  0.00),
('Transporte', 15.00);

-- 4. PRODUCTOS

-- 5. RELACIÓN PRODUCTO_SERVICIOS

-- 6. COMPONENTES (TS, TI, B, TAL, TAC, TC por producto)

-- 8. ÓRDENES

-- 9. ORDEN_PRODUCTOS

-- SHOW TABLES;