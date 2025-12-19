-- 1. Limpiamos por si la tabla ya existía
DROP TABLE IF EXISTS rutas;

-- 2. Creamos una tabla lógica para el tema del ejercicio
CREATE TABLE rutas (
    id SERIAL PRIMARY KEY,
    nombre_ruta VARCHAR(100) NOT NULL,
    distancia_km DECIMAL NOT NULL,
    dificultad VARCHAR(20)
);

-- 3. Insertamos un dato de prueba
INSERT INTO rutas (nombre_ruta, distancia_km, dificultad) 
VALUES ('Camino de Santiago', 780.5, 'Alta');