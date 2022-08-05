import os

class directorio:


    def __init__(self, directorio1:str):
        self.directorio1 = directorio1

    def diccionarioderutas(self,directorio2):
        rutas = os.listdir(directorio2)
        diccionario_de_respuesta = {'nombre': rutas}
        print(diccionario_de_respuesta)
        diccionario_de_respuesta['archivosconmayorpeso'] = {}
        for j in diccionario_de_respuesta["nombre"]:
            print(j)
            print(os.path.abspath(j))
"""""
        rutas=os.listdir(directorio2)
        diccionario_de_respuesta = {'nombre':rutas}
        print(diccionario_de_respuesta)
        diccionario_de_respuesta['archivosconmayorpeso'] = {}
        for j in diccionario_de_respuesta["nombre"]:
            print(j)
            print(rutas)
            print(os.path.abspath(j))
"""""

"""""
for (root,dirs,files) in os.walk('Test', topdown=true): 
        print (root) 
        print (dirs) 
        print (files) 
        print ('--------------------------------') 

Este método crea un nuevo diccionario con claves a partir de un tipo de dato secuencia. El valor de value por defecto es el tipo None.

>>> secuencia = ('python', 'zope', 'plone')
>>> versiones = dict.fromkeys(secuencia)
>>> print "Nuevo Diccionario : %s" %  str(versiones)
Nuevo Diccionario : {'python': None, 'zope': None, 'plone': None}
En el ejemplo anterior inicializa los valores de cada clave a None, mas puede inicializar un valor común por defecto para cada clave:

>>> versiones = dict.fromkeys(secuencia, 0.1)
>>> print "Nuevo Diccionario : %s" %  str(versiones)
Nuevo Diccionario : {'python': 0.1, 'zope': 0.1, 'plone': 0.1}
"""

direc=directorio("C:\pruebas\carpeta1")
direc.diccionarioderutas("C:\pruebas\carpeta1")
