# modulos para archivos dmx
este es un proyecto creado en pyton y que utiliza modulos para lograr que el proyecto sea reutizable, su funcionalidad es recorrer dos carpetas y filtrar archivos dmx, entre estos archivos se puede seleccionar una de varias funciones que existen para asi ver la imformacion que necesite como por ejemplo la ultima fecha de modificacion
## explicacion de cada clase 
> - esto lo hago en el codigo
## requerimientos obligatorios para iniciar el proyecto
> - las rutas de la carpeta dir1 y dir2 deben existir y deben ser rutas diferentes
> - se debe seleccionar almenos una de las opciones de las funciones 
>>  las cuales son:
>> - -size
>> - -modification_date
>> - -fingerprint
> - la ruta output no debe existir pero debe ser una ruta valida


## imformacion adicional
>  usage: main.py [-h] --dir1 DIR1 --dir2 DIR2 [--size] [--modification_date] [--fingerprint] --output OUTPUT

> modulo para filtrar archivos dmx

> options:

|Forma larga|Forma abreviada|Requerido|Descripción|
|---|---|---|---|
|--help|-h|No|show this help message and exit|
|--dir1|-1|Sí|directorio uno con archivos dmx|
|--dir2|-2|Sí|directorio dos con archivos dmx|
|--size|-s|No|diferencar archivos dmx por tamaño|
|--modification_date|-d|No|diferenciar archivos dmx por fecha de modificacion|
|--fingerprint|-f|No|diferenciar archivos dmx por figerprint|
|--output|-o|Sí| ruta del archivo json que se va a crear con los resultados|


## pasos para inciar la aplicacion 
> - primero importar las librerias
> - ejecutar main.py
> - escribir la ruta de la primera carpeta
> - escribir la ruta de la segunda carpeta
> - escribiir que funcion desea realizar
> - escribir una ruuta de salida que no exista
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


>puedes encontrar toda la documentacion de este proyecto en este enlace [documento compartido](https://docs.google.com/document/d/1dEbk0qI2qlFbcdrTo5B1w-_0NxUv8osXjdjIssEdNR0/edit#heading=h.3ti6jx56udpj).