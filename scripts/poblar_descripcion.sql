CREATE OR REPLACE FUNCTION populate_descripcion()
RETURNS void AS $$
DECLARE
    rec RECORD;
    random_text VARCHAR(500);
    text_length INT := 100; 
BEGIN
    FOR rec IN SELECT * FROM actividad_economica LOOP
        random_text := array_to_string(ARRAY(
            SELECT 
                CASE 
                    WHEN random() < 0.15 THEN ' '
                    ELSE chr((65 + round(random() * 25))::integer) 
                END
            FROM generate_series(1, text_length)
        ), '');

        UPDATE actividad_economica
        SET descripcion = random_text
        WHERE padni = rec.padni
          AND ddni = rec.ddni
          AND idni = rec.idni
          AND codigo = rec.codigo;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

