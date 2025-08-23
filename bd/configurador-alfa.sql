-- Borrar base de datos si existe
DROP DATABASE IF EXISTS configurador_alfa;

-- Crear base de datos
CREATE DATABASE configurador_alfa;
USE configurador_alfa;

-- Tabla clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    razon_social VARCHAR(150) NOT NULL,
    rfc VARCHAR(20),
    nombre VARCHAR(100),
    codigo_postal VARCHAR(5),
    direccion TEXT,
    numero_telefono VARCHAR(10),
    correo VARCHAR(100),
    destino TEXT
);

-- Tabla costos
CREATE TABLE costos (
    id_costo INT PRIMARY KEY AUTO_INCREMENT,
    tipo_madera VARCHAR(50) NOT NULL,
    costo DECIMAL(10,2) NOT NULL  -- costo por unidad de volumen 
);

-- Tabla productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50),
    subtipo VARCHAR(50),
    acomodo VARCHAR(50),
    precio_unit DECIMAL(10,2),       -- calculado
    largo_gral DECIMAL(10,2),
    ancho_gral DECIMAL(10,2),
    grosor_gral DECIMAL(10,2)
);

-- Tabla componentes
CREATE TABLE componentes (
    id_componente INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    tipo VARCHAR(20),              -- 'TS', 'TI', 'B', 'TA', 'TC'
    cantidad INT NOT NULL,
    largo DECIMAL(10,2),
    ancho DECIMAL(10,2),
    grosor DECIMAL(10,2),
    tolerancia VARCHAR(100),
    separacion_TS DECIMAL(10,2),   -- opcional
    tipo_B VARCHAR(50),            -- opcional
    distancia_B DECIMAL(10,2),     -- opcional
    id_costo INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    FOREIGN KEY (id_costo) REFERENCES costos(id_costo)
);

-- Tabla servicios
CREATE TABLE servicios (
    id_servicio INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    costo DECIMAL(10,2) NOT NULL
);

-- Relación producto_servicios
CREATE TABLE producto_servicios (
    id_producto_servicio INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    id_servicio INT NOT NULL,
    color VARCHAR(50),               -- Solo aplica si es pintura
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio)
);

-- Tabla ordenes
CREATE TABLE ordenes (
    id_orden INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_estimado DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla orden_productos
CREATE TABLE orden_productos (
    id_orden_producto INT PRIMARY KEY AUTO_INCREMENT,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- USE configurador_alfa;
-- SHOW TABLES;