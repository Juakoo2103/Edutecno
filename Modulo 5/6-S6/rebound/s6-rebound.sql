GRANT ALL PRIVILEGES ON DATABASE s6_rebound TO postgres;

BEGIN;

SAVEPOINT uno;

CREATE TABLE empresa(
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(30),
    direccion VARCHAR(255),
    telefono VARCHAR(11),
    correo VARCHAR(255),
    web VARCHAR(40)
);

CREATE TABLE cliente(
    rut VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(30),
    correo VARCHAR(255),
    direccion VARCHAR(255),
    celular VARCHAR(11),
    alta BOOLEAN
);

CREATE TABLE tipo_vehiculo(
    tipo_vehiculo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE marca(
    marca_id SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE vehiculo(
    vehiculo_id SERIAL PRIMARY KEY,
    patente VARCHAR(6),
    modelo VARCHAR(255),
    color VARCHAR(255),
    PRECIO MONEY,
    frecuencia_mantencion INT,
    marca_id INT,
    tipo_vehiculo_id INT
);

CREATE TABLE venta(
    folio SERIAL PRIMARY KEY,
    fecha DATE,
    monto INT,
    rut_cliente VARCHAR(9),
    vehiculo_id INT
);

CREATE TABLE mantencion(
    mantencion_id SERIAL PRIMARY KEY,
    fecha DATE,
    trabajos_realizados VARCHAR(255),
    folio INT
);

--sección de insección de datos
SAVEPOINT dos;

--Inserte los datos de una empresa.
INSERT INTO
    empresa
VALUES
(
        '9999999999-9',
        'Ono-fio',
        'Santiago',
        '9623659',
        'onofrio@onofrio.cl',
        'onofrio.com'
    );

SELECT
    *
FROM
    empresa;

SAVEPOINT tres;

--Inserte 2 tipos de vehículo.
INSERT INTO
    tipo_vehiculo(nombre)
VALUES
    ('Carga');

INSERT INTO
    tipo_vehiculo(nombre)
VALUES
    ('Transporte');

SELECT
    *
FROM
    tipo_vehiculo;

SAVEPOINT cuatro;

--Inserte 3 clientes.
INSERT INTO
    cliente
VALUES
(
        '1345678-1',
        'Fulanito',
        'fulanito@fulanito.cl',
        'Santiago',
        '956854521',
        TRUE
    );

INSERT INTO
    cliente
VALUES
(
        '7563214-2',
        'Perensejo',
        'perensejo@perensejo.cl',
        'Coquimbo',
        '945213632',
        false
    );

INSERT INTO
    cliente
VALUES
(
        '5231451-k',
        'Rodrigo',
        'rodrigo@rodrigo.cl',
        'Concon',
        '95232526',
        TRUE
    );

SELECT
    *
FROM
    cliente;

SAVEPOINT cinco;

--Inserte 2 marcas
INSERT INTO
    marca(nombre)
VALUES
('Hyundai');

INSERT INTO
    marca(nombre)
VALUES
('Toyota');

SELECT
    *
FROM
    marca;

SAVEPOINT seis;

--Inserte 5 vehículos
INSERT INTO
    vehiculo(
        patente,
        modelo,
        color,
        precio,
        frecuencia_mantencion,
        marca_id,
        tipo_vehiculo_id
    )
VALUES
('963PLK', 'M3', 'Negro', 10000000, 6, 1, 2);

INSERT INTO
    vehiculo(
        patente,
        modelo,
        color,
        precio,
        frecuencia_mantencion,
        marca_id,
        tipo_vehiculo_id
    )
VALUES
('875436', 'M5', 'Rosa', 6000000, 3, 2, 1);

INSERT INTO
    vehiculo(
        patente,
        modelo,
        color,
        precio,
        frecuencia_mantencion,
        marca_id,
        tipo_vehiculo_id
    )
VALUES
('741253', 'H7', 'Gris', 9000000, 12, 2, 2);

INSERT INTO
    vehiculo(
        patente,
        modelo,
        color,
        precio,
        frecuencia_mantencion,
        marca_id,
        tipo_vehiculo_id
    )
VALUES
('952137', 'P8', 'Dorado', 5000000, 5, 1, 1);

INSERT INTO
    vehiculo(
        patente,
        modelo,
        color,
        precio,
        frecuencia_mantencion,
        marca_id,
        tipo_vehiculo_id
    )
VALUES
('746328', 'T6', 'Blanco', 15000000, 2, 2, 2);

SELECT
    *
FROM
    vehiculo;

SAVEPOINT siete;

--Inserte 1 venta para cada cliente.
INSERT INTO
    venta(fecha, monto, rut_cliente, vehiculo_id)
VALUES
('2022-01-23', 10000000, '1345678-1', 1);

INSERT INTO
    venta(fecha, monto, rut_cliente, vehiculo_id)
VALUES
('2022-05-24', 6000000, '7563214-2', 2);

INSERT INTO
    venta(fecha, monto, rut_cliente, vehiculo_id)
VALUES
('2022-02-15', 5000000, '5231451-k', 4);

SELECT
    *
FROM
    venta;

SAVEPOINT ocho;

ALTER TABLE
    mantencion
ADD
    CONSTRAINT fk_folio FOREIGN KEY(folio) REFERENCES venta(folio);

ALTER TABLE
    vehiculo
ADD
    CONSTRAINT fk_marca_id FOREIGN KEY(marca_id) REFERENCES marca(marca_id);

ALTER TABLE
    vehiculo
ADD
    CONSTRAINT fk_tipo_vehiculo_id FOREIGN KEY(tipo_vehiculo_id) REFERENCES tipo_vehiculo(tipo_vehiculo_id);

ALTER TABLE
    venta
ADD
    CONSTRAINT fk_rut_cliente FOREIGN KEY(rut_cliente) REFERENCES cliente(rut);

ALTER TABLE
    venta
ADD
    CONSTRAINT fk_vehiculo_id FOREIGN KEY(vehiculo_id) REFERENCES vehiculo(vehiculo_id);

ROLLBACK;

ROLLBACK TO SAVEPOINT dos;

-- Listar todos los vehículos que no han sido vendidos.
SELECT
    v.*
FROM
    vehiculo v
    LEFT JOIN venta vt ON v.vehiculo_id = vt.vehiculo_id
WHERE
    vt.vehiculo_id IS NULL;

-- Listar todas las ventas de enero del 2020 con las columnas: Folio, FechaVenta, MontoVenta, NombreCliente, RutCliente, Patente, NombreMarca, y Modelo.
SELECT
    ve.folio,
    ve.fecha AS FechaVenta,
    ve.monto AS MontoVenta,
    c.nombre AS NombreCliente,
    c.rut AS RutCliente,
    v.patente,
    m.nombre AS NombreMarca,
    v.modelo
FROM
    venta ve
    JOIN cliente c ON ve.rut_cliente = c.rut
    JOIN vehiculo v ON ve.vehiculo_id = v.vehiculo_id
    JOIN marca m ON v.marca_id = m.marca_id
WHERE
    EXTRACT(
        MONTH
        FROM
            ve.fecha
    ) = 1
    AND EXTRACT(
        YEAR
        FROM
            ve.fecha
    ) = 2020;

-- Sumar las ventas por mes y marca del año 2020.
SELECT
    *
FROM
    venta
WHERE
    fecha BETWEEN ('2020-01-01')
    AND ('2020-12-31')
SELECT
    EXTRACT(
        MONTH
        FROM
            ven.fecha
    ) AS mes,
    m.nombre AS marca,
    SUM(ven.monto) AS venta_total
FROM
    venta ven
    JOIN vechilo v ON v.vehiculo_id = v.vehiculo_id
    JOIN marca m ON v.marca_id = m.marca_id
WHERE
    EXTRACT(
        YEAR
        FROM
            ven.fecha
    ) = '2020'
GROUP BY
    mes
ORDER BY
    mes -- Listar Rut y Nombre de las tablas cliente y empresa.
SELECT
    rut,
    nombre
FROM
    cliente
UNION
SELECT
    rut,
    nombre
FROM
    empresa;