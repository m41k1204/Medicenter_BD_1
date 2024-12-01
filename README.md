
# Proyecto Base de Datos Medicenter

Este proyecto consiste en diseñar una base de datos PostgreSQL desde cero, poblarla con datos sintéticos y realizar diversas consultas para explorar técnicas de optimización. Utilizamos `EXPLAIN ANALYZE` para obtener información detallada sobre los procesos de ejecución de consultas en PostgreSQL.

---

## Informe del Proyecto

Un informe detallado, que incluye las metodologías y hallazgos, está disponible en el directorio `utils`: [Proyecto_Medicenter](utils/Proyecto_Medicenter).

---

## Generación de Datos Sintéticos

Para crear conjuntos de datos de diferentes tamaños (1,000; 10,000; 100,000; y 1,000,000 registros), se proporciona un script en Python en el directorio `scripts`: [data_millon](scripts/data_millon).

### Instrucciones

1. **Ajustar los Rangos de los Bucles**: Modifica los rangos del bucle en el script para generar la cantidad de registros deseada. Por ejemplo, para crear 6,000,000 registros para la tabla `persona`, configura el bucle como:

   ```python
   for i in range(6000000):
   ```

2. **Tiempo de Ejecución**: Generar 25 millones de registros toma aproximadamente 25 minutos.

> **Nota**: El script utiliza la librería [Faker](https://faker.readthedocs.io/en/master/) para generar datos sintéticos realistas.

![Ejemplo de datos generados](images/example_data.png)

---

## Configuración de la Base de Datos

### Pasos

1. **Inicializar la Base de Datos**: Ejecuta el script SQL ubicado en `utils/database.sql` para configurar el esquema de la base de datos.

2. **Descargar Archivos CSV**: Recupera los archivos CSV listados en `utils/data_dump.txt`.

3. **Abrir el Shell de psql**: Accede al shell de psql en tu sistema operativo.

4. **Conectar con la Base de Datos**: Dentro del shell de psql, conéctate a tu instancia de base de datos:

   ```sql
   \connect <nombre_base_datos>
   ```

5. **Importar Datos**: Para cada tabla, ejecuta el siguiente comando para importar datos desde el archivo CSV correspondiente:

   ```sql
   COPY <nombre_esquema>.<nombre_tabla> FROM '<ruta_archivo_csv>' DELIMITER ',';
   ```

   > **Nota**: La duración del proceso de importación varía según el volumen de datos, oscilando entre 15 segundos y varios minutos.

6. **Poblar Descripciones**: Para llenar el atributo `descripcion` de la tabla `actividad_economica`, ejecuta el script SQL que se encuentra en `scripts/poblar_descripcion.sql`.

![Diagrama de la Base de Datos](images/database_diagram.png)

---

## Ejecución de Consultas

El directorio `consultas` contiene diversas consultas, incluidas aquellas relacionadas con la creación de índices y ajustes para realizar experimentos con y sin índices.

> **Ejemplo de consulta:**
>
> ```sql
> SELECT * FROM persona WHERE nombre LIKE 'Juan%';
> ```

---

## Experimentación y Análisis

Utilizando `EXPLAIN ANALYZE`, se obtienen análisis detallados de los pasos de ejecución de las consultas en PostgreSQL. Las conclusiones finales, comparaciones entre consultas con y sin índices, y los resultados de `EXPLAIN ANALYZE` están detallados en el informe del proyecto ubicado en el directorio `utils`: [Proyecto_Medicenter](utils/Proyecto_Medicenter).

![Ejemplo de Resultados EXPLAIN ANALYZE](images/explain_analyze_results.png)

---

## Contacto

Para consultas relacionadas con el proyecto o la experimentación con consultas, por favor contáctame:

📧 **Correo**: michael.hinojosa@utec.edu.pe
