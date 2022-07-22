import validaciones
import parametros


# aqui uno todas las validaciones en una sola y utilizo la tabla de verdad de conjuncion
def validaciones_totales():
    if valida() and valida2() and valida3():
        return True
    else:
        return False


# esta es la primera validacion (la carpeta 1 y 2 tienen que ser directorios,la ruta de salida no puede existir la carpeta 1 y 2 tienen que tener al menos 1 archivo)
def valida():
    respuesta = True
    respuesta = (validaciones.esdirectorio(clase_parametros.argumentos.dir1)
                 and validaciones.esdirectorio(clase_parametros.argumentos.dir2)
                 and not validaciones.existe_ruta(clase_parametros.argumentos.output)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir1)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir2)

                 )
    return respuesta


# esta es la validacion2 se debe seleccionar almenos una de las opciones
def valida2():
    respuesta = True
    parseo()
    respuesta = (clase_parametros.argumentos.modificaton_date or clase_parametros.argumentos.size
                 or clase_parametros.argumentos.fingerprint)
    return respuesta


# esta el la validacion 3 la carpeta 1 debe ser diferente de la 2
def valida3():
    respuesta = True
    parseo()
    if clase_parametros.argumentos.dir1 == clase_parametros.argumentos.dir2:
        respuesta = False
    return respuesta