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