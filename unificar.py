import validaciones
import parametros



clase_parametros = parametros.Parametros()

def validaciones_totales():
   if valida() and valida2() and valida3():
       return True
   else: return False

def parseo():
    clase_parametros.argumentos = clase_parametros.opciones.parse_args()

def valida():
    respuesta = True
    parseo()
    respuesta = (validaciones.esdirectorio(clase_parametros.argumentos.dir1)
                 and validaciones.esdirectorio(clase_parametros.argumentos.dir2)
                 and not validaciones.existe_ruta(clase_parametros.argumentos.output)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir1)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir2))
    return respuesta
def valida2():
    respuesta = True
    parseo()
    respuesta = (clase_parametros.argumentos.modificaton_date or clase_parametros.argumentos.size
                 or clase_parametros.argumentos.fingerprint)
    return respuesta
def valida3():
    respuesta = True
    parseo()
    if clase_parametros.argumentos.dir1 == clase_parametros.argumentos.dir2:
        respuesta=False
    return respuesta
def print_argst():
   if validaciones_totales():
      directory1 = clase_parametros.argumentos.dir1
      directory2 = clase_parametros.argumentos.dir2
      salida = clase_parametros.argumentos.output
      print(f'Directorio 1: {directory1}  Directorio 2: {directory2}  salida {salida}')
   else:
      print("nooo pa, intente de nuevo")

