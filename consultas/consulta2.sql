-- Consulta

EXPLAIN ANALYZE 
SELECT 
		o.tipo_operacion,
       COUNT(o.aecodigo) AS total_operaciones,
       SUM(im.costo_por_unidad * u.cantidad) AS costo_total_insumos,
       COUNT(DISTINCT e.pdni) AS total_enfermeras,
       COUNT(DISTINCT d.pdni) AS total_doctores
FROM operacion o
JOIN actividad_economica ae ON o.aecodigo = ae.codigo
JOIN utiliza u ON o.aecodigo = u.ocodigo
JOIN insumo_medico im ON u.im_ns = im.nro_serial
JOIN enfermera e ON u.edni = e.pdni
JOIN doctor d ON ae.ddni = d.pdni
WHERE e.sueldo > 5500 
AND d.sueldo > 250000 
GROUP BY o.tipo_operacion
ORDER BY total_operaciones DESC;

-- Creacion de indices BTREE

CREATE INDEX idx_sueldo_doctor ON doctor USING BTREE (sueldo);
CREATE INDEX idx_sueldo_enfermera ON enfermera USING BTREE (sueldo);

-- Drop de Indice BTREE

DROP INDEX idx_sueldo_doctor;
DROP INDEX idx_sueldo_enfermera;

-- Ajustes para query sin indices, para query con indices, ponerlo en ON.

SET enable_mergejoin TO OFF;        
SET enable_hashjoin TO OFF;        
SET enable_bitmapscan TO OFF ;   
SET enable_sort TO OFF;

-- Vacuum para limpiar la memoria fisica

VACUUM FULL actividad_economica, operacion, insumo_medico, doctor, enfermera

