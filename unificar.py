"""crrear clase AppUnificarDMX
contructor de la clase
dentro de la clase creo funcion recorrer_directorio
dentro de recorrer_Directorio creo una funcion para recorrer el directorio
tips
usar
os.walk
organizar el directorio """
import os
from functools import wraps


class AppUnificarDMX:
    directorio1 = None
    directorio2 = None
    json_salida = None
    bandera_tamano = None
    bandera_fecha = None
    bandera_sha2 = None

    def __init__(self, directorio1: str, directorio2: str, json_salida: str,
                 bandera_tamano: bool=False ,bandera_fecha : bool=False, bandera_sha2:bool = False):
        self.directorio1 = directorio1
        self.directorio2 = directorio2
        self.json_salida = json_salida
        self.bandera_tamano = bandera_tamano
        self.bandera_fecha = bandera_fecha
        self.bandera_sha2 = bandera_sha2
        self.lista = None

    def listar_directorio(self, directorio):
        self.lista = os.listdir(directorio)

    def ejecutar(self,):
        "correr"
        self.listar_directorio(self.directorio1)
        data = self.decorador(self.invocar_decorador)
        data(self.tamano,self.fecha_modificacion,self.sha2, lista=self.lista, param2='b')
        print(data.__doc__)


    def invocar_decorador(self):
        pass

    def tamano(self):
        print("el tamaño fue de tales")

    def fecha_modificacion(self):
        print("funcion fecha de modificacion")


    def sha2(self):
        print("funcion para sha2")



    def decorador(self,func):
        @wraps(func)
        def funcioninterior(*args,**kwargs):
            '''
            Los argumentos posicionales son las funciones realizar dentro del ciclo
            Los argumentos keywprds son los parametros para ejecutar las funciones
            :param args:
            :param kwargs:
            :return:
            '''
            #print(argumentos.paramtros.argumetos.size)
            print(args)
            print(kwargs)
            print(kwargs["lista"])
            for archive in kwargs["lista"]:
                for funcion in args:
                    print(f"se ejecuta {archive} con {funcion.__name__}")
                    funcion()

        return funcioninterior

#------------------------------------------------------------------------------------------
