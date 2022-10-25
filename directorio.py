import core
import os
import sys


sys.path.append('C:/Users/juanc/PycharmProjects/modulo_dmx')
from file1 import File




class directorio:


    def __init__(self):
        self.directorio1 = directorio
        self.index = None

    def __iter__(self):
        #if self.use_full_path:
        #    return iter(self.get_file_full_paths())
        #return iter(self.get_file_relative_paths())
        return iter(self.index)

    def modi(self):
        import os
        import time

        path = "C:\pruebas\carpeta1"

        modificacion = []
        rutacompleta=[]
        lista = os.listdir(path)
        for filename in lista:
            rutacompleta = os.path.join(path,filename)
            obtenertiempo = os.path.getmtime(rutacompleta)
            fecham = time.ctime(obtenertiempo)
            modificacion.append((fecham))

        return modificacion

    def create_index(self):
        self.index = []

        for root, dirs, files in core.os.walk("C:\pruebas\carpeta1"):
            for f in files:
                full_path = core.os.path.join(root, f)

                tmp_file = core.File(full_path, "C:\pruebas\carpeta1")
                self.index.append(tmp_file)

                # Imprime las tres partes del File para probar self.use_full_path


    def diccionarioderutas(self,directorio):
        """""
        esta funcion sirve para crear una lista con los nombres de todos los archivos que se encuentren en un directorio
        despues crea un dicciorio el cual cada nombre de archivo contenga su ruta
        el diccionario debe contener esta estructura :

        {
	"01010000.dmx": {
		"D:/carpeta1":{
			"ruta": "D:/carpeta1",
			"tamano": 300
		},
		"Z:/carpeta_dmx":{
			"ruta": "Z:/carpeta_dmx/2022/01/01",
			"tamano": 72000
		}
	},
	"01010001.dmx": {
		"D:/carpeta1":{
			"ruta": "D:/carpeta1",
			"tamano": 300
		},


        :param
        """
        rutas=[]
        rutasyarchivos=[]
        modificacion=[]
        numero={}
        final=0
        diccionario_de_respuesta = {}
        for root, dirs, files in os.walk(directorio):
            for file in files:
                modificacion = self.modi()
                rutasyarchivos=os.path.join(root,file)
                rutas.append((file,rutasyarchivos,modificacion))

                #numero=1
                #modificacion = modificacion[numero]
        global key
        global value
        for elemento in rutas:
            key = elemento[0]
            value = elemento[1]
            key1 = elemento[2][1]

            if not key in diccionario_de_respuesta:
                diccionario_de_respuesta[key] = {}

            if not value in diccionario_de_respuesta:
                diccionario_de_respuesta[key][value] = {}

#crear el archivo __init__.py

                import sys
                sys.path.append('C:/Users/juanc/PycharmProjects/modulo_dmx')
                from file import File

           ##esto es una prueba
            #if not key1 in diccionario_de_respuesta:
              #  diccionario_de_respuesta[key][value][key1]={}

                #module = __import__('pruebas3')
                #print(module)
                #func = getattr(module, 'calcular_peso')
                #func()
                funcionaejecutar = getattr(File,'peso')
                # usted es una instanceof
                ruta="hola"
                funcionaejecutar()

                diccionario_de_respuesta[key][value]['peso']=funcionaejecutar()
                diccionario_de_respuesta[key][value][ruta] = ruta
                #diccionario_de_respuesta[key][value][funcionaejecutar()] = {}




        print(diccionario_de_respuesta)
        #print(modificacion)
        #print(f"rutas{rutas}")



    def funcioninterior(self,*args):

        diccionario_de_respuesta = {}

        for elemento in self.index:
            archivo = elemento.name  # archivo dmx
            ruta = elemento.path  # subcarpetas
            rutabase = elemento.base_path  # ruta base
            if not archivo == diccionario_de_respuesta:
                diccionario_de_respuesta[archivo] = {}
            if not rutabase in diccionario_de_respuesta:
                diccionario_de_respuesta[archivo][rutabase] = {}
            if not ruta in diccionario_de_respuesta:
                diccionario_de_respuesta[archivo][rutabase]['ruta'] = ruta



            for funcionaejecutar in args:

                #print(funcionaejecutar(elemento.get_full_path()))
                diccionario_de_respuesta[archivo][rutabase][funcionaejecutar.__name__] = funcionaejecutar(elemento.get_full_path())
        print(core.json.dumps(diccionario_de_respuesta,indent=4))
        print(diccionario_de_respuesta)





direc=directorio()
direc.create_index()
direc.funcioninterior(File.calculate_fingerprint)


