import os

class directorio:


    def __init__(self):
        self.directorio1 = directorio

    def diccionarioderutas(self,directorio):
        rutas=[]
        rutasyarchivos=[]
        rutasyarchivos2 = []
        nivel=0
        diccionario_de_respuesta = {}
        for root, dirs, files in os.walk(directorio):
            print(f"el nombre de la carpeta es {root}")
            print(f"la subcarpeta en {root} es {dirs}")
            if not dirs:
                print("oh mira no hay mas carpetas dentro de esta")
                nivel=nivel-1

            nivel =nivel+1
            print(f"usted esta en el nivel {nivel}")
        for elemento in rutas:
            key = elemento[0]
            value = elemento[1]
            diccionario_de_respuesta[key] = {}
            diccionario_de_respuesta[key][value] = value
            diccionario_de_respuesta[key][value] = {}

       ## print(diccionario_de_respuesta)


direc=directorio()
direc.diccionarioderutas("C:\pruebas\carpeta1")

"""""

                #1)usar arg para trear las funciones y uar su opcion de llamable para ejecutarlas de una vez esto hace que elimine el gettattr
                #2) usar el kwargs pero pues esta si es mas complicada por que tengo que tener una lista de kwargs
                for listafunciones in kwargs["lista"]:
            #import sys
           # sys.path.append('C:/Users/juanc/PycharmProjects/modulo_dmx')
           # from file import File

                    funcionaejecutar = getattr(module, listafunciones,'no_hubo_funcion')
                    funcionaejecutar()
                    diccionario_de_respuesta[archivo][rutabase]['nombredefuncion'] = funcionaejecutar()

                    #for archive in kwargs["lista"]:
                #for funcion in args:
                    #print(f"se ejecuta {archive} con {funcion.__name__}")
                    #funcion1 =funcion()
                    #diccionario_de_respuesta[funcion1]={}
                    #funcion()
"""""