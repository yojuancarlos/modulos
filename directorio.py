import os

class directorio:


    def __init__(self):
        self.directorio1 = directorio

    def diccionarioderutas(self,directorio):
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

        diccionario_de_respuesta['archivosysuruta'] = {}
        for elemento in rutas:
            key = elemento[0]
            value = elemento[1]
            diccionario_de_respuesta['archivosysuruta'][key] = value

        print(diccionario_de_respuesta)
"""""
for root,dirs,files in os.walk(directorio, topdown=True): 
        print (root) 
        print (dirs) 
        print (files) 
        print ('--------------------------------') 

"""

direc=directorio()
direc.diccionarioderutas("C:\pruebas\carpeta1")
