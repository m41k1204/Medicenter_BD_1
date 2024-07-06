-- Consulta

EXPLAIN ANALYZE
SELECT
  AVG(porcentaje_costo_insumos) AS promedio_porcentajes
FROM (
  SELECT
    (SUM(u.cantidad * i.costo_por_unidad) / a.monto) * 100 AS porcentaje_costo_insumos
  FROM utiliza u
  JOIN insumo_medico i
    ON u.im_ns = i.nro_serial
  JOIN operacion o
    ON o.aecodigo = u.ocodigo
  JOIN actividad_economica a
    ON a.codigo = o.aecodigo
  WHERE  
	i.costo_por_unidad > 95 
	GROUP BY o.aecodigo, a.monto
) subquery;

-- Creacion de Indice BTREE

CREATE INDEX idx_insumo_medico_costo_por_unidad ON insumo_medico USING BTREE (costo_por_unidad);

-- Drop de Indice BTREE

DROP INDEX idx_insumo_medico_costo_por_unidad

-- Ajustes para query sin indices, para query con indices, ponerlo en ON.

SET enable_mergejoin TO OFF;        
SET enable_hashjoin TO OFF;        
SET enable_bitmapscan TO OFF ;   
SET enable_sort TO OFF;

-- Vacuum para limpiar la memoria fisica

VACUUM FULL actividad_economica, operacion, insumo_medico, utiliza


