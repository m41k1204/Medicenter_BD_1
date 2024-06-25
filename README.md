# Medicenter_BD_1

## Este es un modelado de una base de datos para un policlínico en PostgreSQL

Para inicializar la data en la base de datos seguir las siguientes instrucciones:
1. Descargar los CSVs del data_dump que encontraran en utils -> data_dump.txt
2. Abrir la consola de psql-shell en windows u otro sistema operativo.
3. En la consola hacer cuatro enters, deberia salir algo asi:
4. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/702dcdbf-286b-4280-b434-f18d752e4863)
5. En la parte de la contraseña ingresar la contraseña del pgadmin. Tras una coneccion exitosa deberia de salir algo asi:
6. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/e71775c5-606a-4507-8881-806426ee7580)
7. Ahi conectarse a la instancia de base de datos creada en el pgadmin:
```bash
\connect <nombre_de_la_bd>
```
8. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/cd8dfc42-45bf-422e-8dfa-6bf144647137)
9. Una vez en la base de datos ejecutar el siguiente comando para cada tabla, deberia de haber creado el esquema en el pgadmin.
```bash
COPY <nombre_esquema>.<nombre_tabla> FROM '<direccion_csv>' DELIMITER ',';
```
10. ![image](https://github.com/m41k1204/Medicenter_BD_1/assets/155772773/93ce5ab7-f16c-45a6-a1f5-a31718d7a93c)
11. El proceso de copia dura de 15 segundos a un par de minutos, dependiendo de la cantidad de datos que haya en el csv.
12. Por último, tras una copia exitosa debería de salir un mensaje asi:
```bash
COPY 6000000
```



