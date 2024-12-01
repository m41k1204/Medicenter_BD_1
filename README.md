# Proyecto de Fin de Curso - Base de Datos 1 (CS 2041)

Este proyecto tiene como objetivo modelar desde cero una base de datos en PostgreSQL. Tras poblarla con datos ficticios, se realizan consultas para explorar diversas formas de optimización y, con la ayuda de `EXPLAIN ANALYZE`, entender el proceso interno de PostgreSQL al ejecutar consultas.

📄 **Informe completo**: Toda la información detallada del proyecto se encuentra en [`utils/Proyecto_Medicenter`](utils/Proyecto_Medicenter).

---

## Tabla de Contenidos

- [Introducción](#proyecto-de-fin-de-curso---base-de-datos-1-cs-2041)
- [Creación de Dummy Data](#creación-de-dummy-data)
  - [Pasos para ajustar el tamaño](#pasos-para-ajustar-el-tamaño)
  - [Librerías utilizadas](#librerías-utilizadas)
- [Creación de la Base de Datos](#creación-de-la-base-de-datos)
  - [Instrucciones](#instrucciones)
- [Ejecución de Consultas](#ejecución-de-consultas)
- [Experimentación](#experimentación)
- [Características](#características)
- [Contribuciones](#contribuciones)
- [Contacto](#contacto)

---

## Creación de Dummy Data

Para generar los 25 millones de datos del esquema, se utilizó un script en Python ubicado en `scripts/data_millon`. Este script permite generar tablas con diferentes tamaños de datos:

- Mil registros
- Diez mil registros
- Cien mil registros
- Un millón de registros

### Pasos para ajustar el tamaño:
1. Modifica el rango en los bucles `for` dentro del script según el tamaño deseado.
   - Ejemplo: Para crear 25 millones de datos, usa:
     ```python
     for i in range(6000000):
     ```
2. El tiempo estimado para generar 25 millones de datos es aproximadamente **25 minutos**.

### Librerías utilizadas:
- **Faker**: Genera datos ficticios realistas.
  - Documentación: [https://faker.readthedocs.io/en/master/](https://faker.readthedocs.io/en/master/)

---

## Creación de la Base de Datos

### Instrucciones:
1. **Inicializa la base de datos**:
   - Utiliza el archivo `utils/database.sql`.

2. **Descarga los CSVs**:
   - Ubicados en `utils/data_dump.txt`.

3. **Abre la consola de PostgreSQL**:
   - En Windows u otro sistema operativo, accede al shell de `psql`.
   - Pulsa Enter cuatro veces hasta que veas algo como esto:
     ![Conexión inicial](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/702dcdbf-286b-4280-b434-f18d752e4863)

4. **Ingresa la contraseña**:
   - Escribe la contraseña configurada en `pgAdmin`.
   - Una conexión exitosa se verá así:
     ![Conexión exitosa](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/e71775c5-606a-4507-8881-806426ee7580)

5. **Conéctate a la base de datos**:
   - Usa el comando:
     ```bash
     \connect <nombre_de_la_bd>
     ```
   - Ejemplo de conexión:
     ![Conexión a la base de datos](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/cd8dfc42-45bf-422e-8dfa-6bf144647137)

6. **Copia los datos de los CSVs a las tablas**:
   - Ejecuta:
     ```bash
     COPY <nombre_esquema>.<nombre_tabla> FROM '<direccion_csv>' DELIMITER ',';
     ```
   - Resultado esperado:
     ![Copia de datos](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/93ce5ab7-f16c-45a6-a1f5-a31718d7a93c)

7. **Verifica el resultado**:
   - Un mensaje de éxito será similar a:
     ```bash
     COPY 6000000
     ```

8. **Poblar la descripción de `actividad_economica`**:
   - Ejecuta el archivo `scripts/poblar_descripcion.sql`.

---

## Ejecución de Consultas

Las consultas se encuentran en el directorio `consultas`. Cada archivo incluye:

- La consulta SQL
- Creación de índices adicionales
- Ajustes para experimentar con y sin índices

---

## Experimentación

Durante la experimentación, se utilizó `EXPLAIN ANALYZE` al inicio de las consultas para obtener un análisis detallado de los pasos que realiza PostgreSQL.

### Detalles:
- Comparación entre consultas con y sin índices.
- Resultados detallados de `EXPLAIN ANALYZE`.

Toda la información está documentada en el informe del proyecto: `utils/Proyecto_Medicenter`.

---

## Características

- Modelo relacional optimizado para grandes volúmenes de datos.
- Uso de scripts automatizados para poblar datos.
- Experimentación avanzada con índices.
- Comparación de rendimiento mediante `EXPLAIN ANALYZE`.
- Base de datos escalable para distintos tamaños de datos.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Realiza un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
