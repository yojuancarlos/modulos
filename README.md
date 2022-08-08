# modulos para archivos dmx
este es un proyecto creado en pyton y que utiliza modulos para lograr que el proyecto sea reutizable, su funcionalidad es recorrer dos carpetas y filtrar archivos dmx, entre estos archivos se puede seleccionar una de varias funciones que existen para asi ver la imformacion que necesite como por ejemplo la ultima fecha de modificacion
## explicacion de cada clase 
> - main.py
>> - es el encargado de inciar el proyecto
> - validaciones.py
>> - es un  modulo que contiene funciones basicas de validaciones como saber si es una un directoruio o una archivo
> - parametros.py
>> - en el modulo que se encarga de recibir los argumentos escritos por consola
> - unificar.py
>> - es un modulo que contiene funciones propias del proyecto como por ejemplo pasar  funciones como argumentos

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
