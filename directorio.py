import os

class directorio:


    def __init__(self):
        self.directorio1 = directorio

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
        rutasyarchivos2 = []
        diccionario_de_respuesta = {}
        for root, dirs, files in os.walk(directorio, topdown=True):
            for file in files:
                rutasyarchivos=os.path.join(root,file)
                rutas.append((file,rutasyarchivos))
                #print(f"{os.path.join(root,file)}")
               # print(type(os.path.join(root,file)))
        for elemento in rutas:
            key = elemento[0]
            value = elemento[1]
            diccionario_de_respuesta[key] = {}
            diccionario_de_respuesta[key][value] = value
            diccionario_de_respuesta[key][value] = {}

        print(diccionario_de_respuesta)


direc=directorio()
direc.diccionarioderutas("C:\pruebas\carpeta1")
help(direc)