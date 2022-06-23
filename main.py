import argparse
import sys
import json
import os
import re
import time
from datetime import datetime
#hasta aqui las importaciones
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--dir1','-1',type=str,required=True,help='selecciona la ruta de la carpeta 1')
	parser.add_argument('--dir2','-2',type=str,required=True,help='selecciona la ruta de la carpeta 2')
	parser.add_argument('--operation', required=False,type=str,default='',help='una vez halla ingresado ambas carpetas escriba con la letra  el proceso que desee realizar (para ver la lista de procesos ve a la documentacion escrita en el repositorio de  git hub )')
	args=parser.parse_args()
	sys.stdout.write(str(funciones(args)))


def funciones(args):
	#listar los directorios y usar teoria de conjuntos
	lista_carpeta1 = os.listdir(args.dir1)
	lista_carpeta2 = os.listdir(args.dir2)
	m = set(lista_carpeta1)
	m2 = set(lista_carpeta2)
	archivosrepetidos = m & m2
	archivosdiferentes = m - m2
	archivosdiferentes2 = m2 - m
	#creo el diccionario
	diccionario_de_respuesta = {'ambas_carpetas': list(archivosrepetidos),
								'solo_carpeta1': list(archivosdiferentes),
								'solo_carpeta2': list(archivosdiferentes2)}
#compruebo si es un directorio existente
	esdirectorio1=  os.path.isdir(args.dir1)
	esdirectorio2 = os.path.isdir(args.dir2)
	#------------------------------------------------------------
	#validadaciones
	if esdirectorio1 == False :
		resultado = print("la carpeta 1 no existe por favor escriba uan carpeta valida")
	elif esdirectorio2 == False:
		resultado = print("la carpeta 2 no existe por favor escriba uan carpeta valida ")
	elif args.dir1 == args.dir2 :
		resultado = print("ambas carpetas son iguales por favor escriba dos carpetas distintas ")
#-----------------------------------------------
	#aqui son las funciones
	else:
		#funcion para saber cual archivo tiene mañor peso
		if args.operation == 's':
			rutasypeso = []
			for filename in archivosrepetidos:
				variable_de_rutas_de_la_carpeta1 = os.path.join(args.dir1, filename)
				peso_archivo_carpeta1 = os.path.getsize(variable_de_rutas_de_la_carpeta1)

				variable_de_rutas_de_la_carpeta2 = os.path.join(args.dir2, filename)
				peso_archivo_carpeta2 = os.path.getsize(variable_de_rutas_de_la_carpeta2)
				#aqui mira cual es el mas grande
				if peso_archivo_carpeta1 > peso_archivo_carpeta2:
					# print(f"el archivo {filename} mas pesados esta en la {variable_de_rutas_de_la_carpeta1}  y su peso es {peso_archivo_carpeta1}")
					rutasypeso.append((variable_de_rutas_de_la_carpeta1, peso_archivo_carpeta1))

				elif peso_archivo_carpeta2 > peso_archivo_carpeta1:
					# print(f"el archivo {filename} mas pesado esta en la {variable_de_rutas_de_la_carpeta2}  y su peso es {peso_archivo_carpeta12}")
					rutasypeso.append((variable_de_rutas_de_la_carpeta2, peso_archivo_carpeta2))
			diccionario_de_respuesta['archivosconmayorpeso'] = {}

			for elemento in rutasypeso:
				key = elemento[0]
				value = elemento[1]
				diccionario_de_respuesta['archivosconmayorpeso'][key] = value

			resultado = rutasypeso
#funcion para saber la fecha de modificacion de un archivo
		if args.operation == 'd':
			modificacion=[]
			for filename in archivosrepetidos:
				variable_de_rutas_de_la_carpeta1 = os.path.join(args.dir1, filename)
				ti_m = os.path.getmtime(variable_de_rutas_de_la_carpeta1)
				m_ti = time.ctime(ti_m)
				modificacion.append((variable_de_rutas_de_la_carpeta1,m_ti))
			resultado = modificacion
			#funcion para exportar el archivo .json
		if args.operation == 'o':
	#--------------------------
	#usar fecha como nombre del json
			now = datetime.now()

			cadena = ("d")
			with open('data.json', 'w') as file:

				json.dump(diccionario_de_respuesta, file, indent=4)
			resultado= print("el json fue creado con exito")

		#ver la lista de archivos repetidos
		if args.operation == "repetidos":
			resultado =  archivosrepetidos
		#ver la lista de archivo que solo esten en la carpeta 1
		if args.operation == "carpeta1":
			resultado = archivosdiferentes
		#ver la lista de archivos que solo esten en la carpeta 2
		if args.operation == "carpeta2":
			resultado = archivosdiferentes2

	##raise Exception("tales")

	return  resultado

if __name__=='__main__':
	main()
