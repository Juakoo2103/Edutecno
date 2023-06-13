tabla reparto 
id foranea peliculas
actor

tabla peliculas
id 
pelicula
estreno
Director

BEGIN;
SAVEPOINT uno;
CREATE TABLE peliculas(
    id INT PRIMARY KEY,
    pelicula VARCHAR(255),
    estreno INT,
    director VARCHAR(255)
);

CREATE TABLE reparto(
    id_pelicula INT,
    actor VARCHAR(255),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id)
);

COMMIT;

\COPY "peliculas" FROM 'C:\Users\jxako\peliculas\peliculas.csv' WITH CSV;

\COPY "reparto" FROM 'C:\Users\jxako\peliculas\reparto.csv' WITH CSV;



--Listar todos los actores que aparecen en la película "Titanic", indicando el título de la película, 
año de estreno, director y todo el reparto.
SELECT p.pelicula, p.estreno, p.director, r.actor
FROM peliculas p
JOIN reparto r ON p.id = r.id_pelicula
WHERE p.pelicula = 'Titanic';

--Listar los 10 directores más populares, indicando su nombre y cuántas películas aparecen 
en el top 100. 
SELECT p.director, COUNT(*) AS peliculas_en_top_100
FROM peliculas p
WHERE p.id IN (
    SELECT DISTINCT id_pelicula
    FROM reparto
)
GROUP BY p.director
ORDER BY peliculas_en_top_100 DESC
LIMIT 10;

--Indicar cuántos actores distintos hay. 
SELECT COUNT(DISTINCT actor) AS actores_distintos
FROM reparto;

--Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos), ordenadas por título de manera ascendente.
SELECT pelicula, estreno
FROM peliculas
WHERE estreno BETWEEN 1990 AND 1999
ORDER BY pelicula ASC;

--Listar los actores de la película más nueva. 
SELECT r.actor
FROM peliculas p
JOIN reparto r ON p.id = r.id_pelicula
WHERE p.estreno = (
    SELECT MAX(estreno)
    FROM peliculas
);

--Inserte los datos de una nueva película solo en memoria, y otra película en el disco duro. 
CREATE TEMPORARY TABLE peliculas_temporal(
    id INT,
    pelicula VARCHAR(255),
    estreno INT,
    director VARCHAR(255)
);

INSERT INTO peliculas_temporal (id, pelicula, estreno, director)
VALUES (1, 'Nueva película en memoria', 2023, 'Director en memoria');

--Actualice 5 directores utilizando ROLLBACK.
START TRANSACTION;

UPDATE peliculas SET director = 'Nuevo director' WHERE id = 1;
UPDATE peliculas SET director = 'Otro director' WHERE id = 2;
UPDATE peliculas SET director = 'Tercer director' WHERE id = 3;
UPDATE peliculas SET director = 'Cuarto director' WHERE id = 4;
UPDATE peliculas SET director = 'Quinto director' WHERE id = 5;

ROLLBACK;
--Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT
START TRANSACTION;

SAVEPOINT insert_actores;

INSERT INTO reparto (id_pelicula, actor)
SELECT id, 'Nuevo actor' FROM peliculas WHERE pelicula = 'Rambo';

ROLLBACK TO SAVEPOINT insert_actores;

--Elimina las películas estrenadas el año 2008 solo en memoria.
CREATE TEMPORARY TABLE peliculas_a_eliminar AS
SELECT id FROM peliculas WHERE estreno = 2008;

DELETE FROM peliculas WHERE id IN (SELECT id FROM peliculas_a_eliminar);

--Inserte 2 actores para cada película estrenada el 2001.
INSERT INTO reparto (id_pelicula, actor)
SELECT id, 'Nuevo actor' FROM peliculas WHERE estreno = 2001
UNION ALL
SELECT id, 'Otro actor' FROM peliculas WHERE estreno = 2001;

--Actualice la película “King Kong” por el nombre de “Donkey Kong”, sin efectuar cambios en disco duro. 

UPDATE peliculas SET pelicula = 'Donkey Kong' WHERE pelicula = 'King Kong';
