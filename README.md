# mudulos para archivos dmx
este es un proyecto creado en pyton y que utiliza modulos para lograr que el proyecto sea reutizable, su funcionalidad es recorrer dos carpetas y filtrar archivos dmx, entre estos archivos se puede seleccionar una de varias funciones que existen para asi ver la imformacion que necesite como por ejemplo la ultima fecha de modificacion

## librerias que se deben importar
> - argparse
> - os
## lista de funciones

- "--size" o "-s"  esta opcion sirve para ver la lista de los archivos con mayor peso cuando exite un archivo con el mismo nombre en ambas carpetas

- "--modification-date" o "-d" esta opcion sirve para ver la ultima fecha de modificacion  de los archivos cuyo nombre se el mismo

- "--output" o "-o" W esta opcion crea un archivo .json en la carpeta donde esta el proyecto

- "--fingerprint" o "-f" esta opcion muestra el fingerprint

- "--dir1" o "-1" esta opcion sirve para ver los archivos que solo existan em la carpeta 1

- "--dir2" o "-2" esta opcion sirve para ver los archivos que solo existan em la carpeta 2

> si necesita mas ayuda escriba  -h
