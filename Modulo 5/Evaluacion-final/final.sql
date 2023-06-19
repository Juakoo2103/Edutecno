--Aquellas usadas para insertar, modificar y eliminar un Customer, Staff y Actor.

# CUSTOMER
INSERT INTO customer VALUE (customer_id, store_id, first_name, last_name, email, addres_id, activebool, create_date, last_update,active);

# Se setea un customer_id al ser valor unico a encontra
UPDATE customer SET columna WHERE customer_id = valor;

# Se setea un customer_id al ser valor unico a encontra
DELETE FROM customer WHERE customer_id = valor;

# STAFF
INSERT INTO staff VALUE (staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update, picture);

# Se setea un staff_id al ser valor unico a encontra
UPDATE staff SET parametro_nuevo WHERE staff_id = valor;

# Se setea un staff_id al ser valor unico a encontra
DELETE FROM staff WHERE staff_id = valor;

# ACTOR 
INSERT INTO actor VALUE (actor_id, first_name, last_name, last_update);

# Se setea un actor_id al ser valor unico a encontra
UPDATE actor SET parametro_nuevo WHERE actor_id = valor;

# Se setea un actor_id al ser valor unico a encontra
DELETE FROM actor WHERE actor_id = valor;


--Listar todas las “rental” con los datos del “customer” dado un año y mes.

SELECT rental.* from rental r
JOIN customer
ON r.customer_id = customer.customer_id 
WHERE EXTRACT(YEAR FROM r.rental_date) = '2005'
AND
EXTRACT(MONTH FROM r.rental_date) = '05' 


--Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”.

SELECT payment_id as numero_payment, payment_date as fecha, amount as total 
FROM payment 
ORDER BY fecha asc;

--Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0.

SELECT title,  
FROM film 
WHERE rental_rate > 4 AND release_year ='2006'
ORDER BY rental_rate asc;

--Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, si éstas pueden ser nulas, y su tipo de dato correspondiente.

SELECT
    t1.TABLE_NAME AS tabla_nombre,
    t1.COLUMN_NAME AS columna_nombre,
    t1.COLUMN_DEFAULT AS columna_defecto,
    t1.IS_NULLABLE AS columna_nulo,
    t1.DATA_TYPE AS columna_tipo_dato,
    COALESCE(t1.NUMERIC_PRECISION,
    t1.CHARACTER_MAXIMUM_LENGTH) AS columna_longitud,
    PG_CATALOG.COL_DESCRIPTION(t2.OID,
    t1.DTD_IDENTIFIER::int) AS columna_descripcion,
    t1.DOMAIN_NAME AS columna_dominio
FROM 
    INFORMATION_SCHEMA.COLUMNS t1
    INNER JOIN PG_CLASS t2 ON (t2.RELNAME = t1.TABLE_NAME)
WHERE 
    t1.TABLE_SCHEMA = 'public'
ORDER BY
    t1.TABLE_NAME;