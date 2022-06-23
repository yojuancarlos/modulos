# mudulos para archivos dmx
este es un proyecto creado en pyton cuya funcionalidad es recorrer dos carpetas y filtrar archivos dmx, entre estos archivos se puede seleccionar una de varias funciones que existen para asi ver la imformacion que necesite como por ejemplo la ultima fecha de modificacion


antes de comenzar la lista debo aclarar que para que funcione todo correctamente primero debe incresar las rutas de las dos carpetas correctamente y que las carpetas no deben ser iguales despues de esto escriba --operation y unicamente la letra del proceso que desee realizar ejemplo
python modulos_dmx.py -1 C:\pruebas\carpeta1 -2 C:\pruebas\carpeta2 --operation s
si necesita mas ayuda escriba python modulos_dmx.py -h

##lista de comando 

"s"  esta opcion sirve para ver la lista de los archivos con mayor peso cuando exite un archivo con el mismo nombre en ambas carpetas
"d" esta opcion sirve para ver la ultima fecha de modificacion  de los archivos cuyo nombre se el mismo
"o" esta opcion crea un archivo .json en la carpeta donde esta el proyecto
"repetidos" esta opcion muestra la lista de los archivos con el mismo nombre que existen tanto en la carpeta 1 como la carpeta 2
"carpeta1" esta opcion sirve para ver los archivos que solo existan em la carpeta 1
"carpeta2" esta opcion sirve para ver los archivos que solo existan em la carpeta 2
