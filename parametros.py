import validaciones
import argparse

class Parametros:
    """
    Clase Parametros

    Se basa en la librería argparse (https://docs.python.org/3/library/argparse.html).

    Se encarga de crear dinámicamente los parámetros o argumentos para una aplicación.

    @opciones       Instancia de AgumentParser
    @argumentos     Datos parseados. Antes de ser parseado el valor que tiene es None.
    """

    opciones = None
    argumentos = None

    def __init__(self, desc:str, arguments:dict):
        """
        Constructor

        @desc       Es una cadena de texto que describe la aplicación
        @arguments  Es un diccionario que indica los argumentos a crear. La estructura que debe tener es
                    {
                        "<nombre>":{
                            "name": <nombre de argumento>,
                            ["alias": <alias del argumento>,]
                            [<llave de argumento>: <valor de argumento>[,
                            <llave de argumento>: <valor de argumento>,
                            <llave de argumento>: <valor de argumento>]]
                        }[,
                        "<nombre>":{
                            "name": <nombre de argumento>,
                            ["alias": <alias del argumento>,]
                            [<llave de argumento>: <valor de argumento>[,
                            <llave de argumento>: <valor de argumento>,
                            <llave de argumento>: <valor de argumento>]]
                        }]
                    }

                    Donde:
                        <nombre>:   Un nombre natural para describir el argumento
                        "name":     Esta llave dentro del JSON/diccionario es un argumento obligatorio
                        <nombre de argumento>: El valor que se le va a asigna a "name" y es el campo
                                    posicional en add_argument que inicia con "--".
                        "alias":    Esta llave dentro del JSON/diccionario es un argumento opcional
                        <alias del argumento>: El valor que se le va a asiganar a "alias" y es el campo
                                    posicional en add_argument que inicia con "-"
                        <llave de argumento>: (Opcional)Es el nombre del argumento tipo keyword dentro de
                                    losvalores de add_argument. Estos valores deben ser los mismos que la
                                    documentacion de argparse.
                        <valor de argumento>: Es el valor que se le asigna a su respectiva llave de
                                    argumento y que se indica en la documentación de argparse.

                    Se recomienda que se tenga las siguientes llaves en el JSON/dict: name, alias, required
                    y help
        """
        self.opciones = argparse.ArgumentParser(description=desc)
        for nombre_arg, datos_arg in arguments.items():
            # Validación necesaria
            if 'name' in datos_arg:
                nombre = datos_arg['name']
                
                kwargumentos = {}
                opciones_kwargumentos = ['action', 'help', 'required']
                for kwargumento in opciones_kwargumentos:
                    if kwargumento in datos_arg:
                        kwargumentos[kwargumento] = datos_arg[kwargumento]
                if 'alias' in datos_arg:
                    self.opciones.add_argument('--'+nombre, '-'+datos_arg['alias'], **kwargumentos)
                else:
                    self.opciones.add_argument('--'+nombre, **kwargumentos)
            else:
                raise Exception(f'No hay dato de nombre para el argumento {nombre_arg}')

    def parseo(self):
        self.argumentos = self.opciones.parse_args()

    #si todas las validaciones se cumplen se puede imprimir el mensaje
    def print_argst(self):
        if self.argumentos not is None:
            print(self.argumentos)






