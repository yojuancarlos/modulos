"""crrear clase AppUnificarDMX
contructor de la clase
dentro de la clase creo funcion recorrer_directorio
dentro de recorrer_Directorio creo una funcion para recorrer el directorio
tips
usar
os.walk
organizar el directorio """
import os


class AppUnificarDMX:
    directorio1 = None
    directorio2 = None
    json_salida = None
    bandera_tamano = None
    bandera_fecha = None
    bandera_sha2 = None

    def __init__(self, dierectorio1: str, directorio2: str, json_salida: str,
                 bandera_tamano: bool=False ,bandera_fecha : bool=False, bandera_sha2:bool = False):
        self.directorio1 = dierectorio1
        self.directorio2 = directorio2
        self.json_salida = json_salida
        self.bandera_tamano = bandera_tamano
        self.bandera_fecha = bandera_fecha
        self.bandera_sha2 = bandera_sha2
        pass

    def recorrer_directorio(self, directorio):
        lista = os.listdir(directorio)
        print(lista)

    def ejecutar(self):






