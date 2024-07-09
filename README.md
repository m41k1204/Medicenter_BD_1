# Proyecto de fin de Curso - Base de Datos 1 (CS 2041)

## Este proyecto tiene el objetivo de modelar desde cero una base de datos y tras poblarla con datos ficticios, experimentar sobre ella con consultas que permitan entender las diversas formas en las que se pueden optimizar y de la ayuda de ```Explain Analyze``` entender el proceso que hace PostgreSQL cada vez que corre una consulta.

El informe detallado con toda la información se encuentra en utils -> Proyecto_Medicenter


## Creación de dummy data
Para la creación de los 25 millones de datos para el esquema de millones de datos, que son los que más demoran, se utilizó un script de python que se encuentra en scripts -> data_millon.
Este script fue utilizado para la creación de los cuatro esquemas que contienen tablas con mil, diez mil, cien mil y un millón de datos. Para variar entre la creción de los cuatro esquemas, se tiene que agregar o disminuir los ceros en todos los for loops de forma equitativa.
La duración para la creación de los 25 millones de datos (el for loop de persona debería de tener ```for i in range(6000000)```) es de aprox. 25 minutos.
Para la elaboración de la data data se utilizó la librería de python Faker: https://faker.readthedocs.io/en/master/

## Creación de Base de datos
Para inicializar la data en la base de datos seguir las siguientes instrucciones:
1. Inicializar la base de datos con el archivo database.sql en utils -> database.sql
2. Descargar los CSVs del data_dump que encontraran en utils -> data_dump.txt
3. Abrir la consola de psql-shell en windows u otro sistema operativo.
4. En la consola hacer cuatro enters, deberia salir algo asi:
5. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/702dcdbf-286b-4280-b434-f18d752e4863)
6. En la parte de la contraseña ingresar la contraseña del pgadmin. Tras una conexión exitosa debería de salir algo asi:
7. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/e71775c5-606a-4507-8881-806426ee7580)
8. Ahí conectarse a la instancia de base de datos creada en el pgadmin:
```bash
\connect <nombre_de_la_bd>
```
9. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/cd8dfc42-45bf-422e-8dfa-6bf144647137)
10. Una vez en la base de datos ejecutar el siguiente comando para cada tabla, deberia de haber creado el esquema en el pgadmin.
```bash
COPY <nombre_esquema>.<nombre_tabla> FROM '<direccion_csv>' DELIMITER ',';
```
11. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/93ce5ab7-f16c-45a6-a1f5-a31718d7a93c)
12. El proceso de copia dura de 15 segundos a un par de minutos, dependiendo de la cantidad de datos que haya en el csv.
13. Por último, tras una copia exitosa debería de salir un mensaje asi:
```bash
COPY 6000000
```
14. Por último, para poblar el atributo descripción de la tabla actividad_economica, ejecutar el código contenido en el archivo poblar_descripcion.sql en scripts -> poblar_descripcion.sql

## Correr las consultas
Las consultas las podrá encontrar en el directorio consultas y cuentan con la consulta, asi como la creación de índices adicionales y demás ajustes para la expetimentación con índices y sin índices.

## Experimentación 
Durante la experimentación se utilizó ```Explain Analyze``` al inicio de las consultas para poder recibir un análisis completo sobre el paso a paso de lo que hace PostgreSQL durante la consulta.
Las conclusiones finales, así como la comparación entre las consultas sin y con índices y los resultados de los explain analyze los puede encontrar en el informe del proyecto en utils -> Proyecto_Medicenter

## Contacto
En caso surgiera una duda sobre el proyecto y/o la experimentación de las consultas, me pueden contacar por mail a
michael.hinojosa@utec.edu.pe






