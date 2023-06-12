CREATE TABLE empresa(
	rut VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(120),
	direccion VARCHAR(120),
	telefono VARCHAR(15),
	correo VARCHAR(80),
	web VARCHAR(50)
);

CREATE TABLE herramienta(
	id_herramienta INT PRIMARY KEY,
	nombre VARCHAR(120),
	precio_dia MONEY
);

CREATE TABLE cliente(
	rut VARCHAR(10) PRIM
	--iniciando una transacción
BEGIN;

--asegurando el primer estado creando un punto de estado
--SAVEPOINT nombre_save_point;
SAVEPOINT primero;

--Inserte 5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);

SAVEPOINT segundo;

--Inserte 3 clientes.
INSERT INTO cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);							  
							  
--si no estoy contento o sucede un error se regresa a pun punto de guardado
ROLLBACK TO SAVEPOINT primero;
ROLLBACK TO SAVEPOINT segundo;

--si estoy contento y sucede todo bien, realizamos un commit
COMMIT;

SELECT * FROM herramienta;
SELECT * FROM cliente;ARY KEY,
	nombre VARCHAR(120),
	correo VARCHAR(80),
	direccion VARCHAR(120),
	celular VARCHAR(15)
);

CREATE TABLE arriendo(
	folio INT PRIMARY KEY,
	fecha DATE,
	dias INT,
	valor_dia INT,
	garantia VARCHAR(30),
	id_herramienta INT,
	rut_cliente VARCHAR(10)
);

ALTER TABLE arriendo 
ADD CONSTRAINT fk_id_herramienta 
FOREIGN KEY(id_herramienta) 
REFERENCES herramienta(id_herramienta);

ALTER TABLE arriendo 
ADD CONSTRAINT fk_rut_cliente 
FOREIGN KEY(rut_cliente) 
REFERENCES cliente(rut);

COMMIT;
SELECT * FROM empresa;
SELECT * FROM herramienta;

--iniciando una transacción
BEGIN;

--asegurando el primer estado creando un punto de estado
--SAVEPOINT nombre_save_point;
SAVEPOINT primero;

--Inserte 5 herramientas.
INSERT INTO herramienta VALUES(1,'Taladro Electrico',10000),
                              (2,'Cierra Electrica',20000),
                              (3,'Pistola de Clavos',30000),
                              (4,'Lijadora',40000),
                              (5,'Serrucho Electrico',50000);

SAVEPOINT segundo;

--Inserte 3 clientes.
INSERT INTO cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
                          ('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
                          ('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);							  
							  
--si no estoy contento o sucede un error se regresa a pun punto de guardado
ROLLBACK TO SAVEPOINT primero;
ROLLBACK TO SAVEPOINT segundo;

--si estoy contento y sucede todo bien, realizamos un commit
COMMIT;

SELECT * FROM herramienta;
SELECT * FROM cliente;