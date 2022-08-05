import os

class directorio:


    def __init__(self):
        self.directorio1 = directorio

    def diccionarioderutas(self,directorio):
        for root, dirs, files in os.walk(directorio, topdown=True):

            for file in files:
                print(file)
                print(f"{os.path.join(root,file)}")
                print(type(os.path.join(root,file)))

    def unirlistas(self):
        lista1=self.diccionarioderutas("C:\pruebas\carpeta1")
        lista2=self.diccionarioderutas("C:\pruebas\carpeta2")


"""""
        diccionario_de_respuesta['archivosconmayorpeso']={}
for elemento in rutasypeso:
    key=elemento[0]
    value=elemento[1]
    diccionario_de_respuesta['archivosconmayorpeso'][key]=value
"""""

"""""
for root,dirs,files in os.walk(directorio, topdown=True): 
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

direc=directorio()
direc.diccionarioderutas("C:\pruebas\carpeta1")
