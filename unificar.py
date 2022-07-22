import validaciones


def valida(clase_parametros):
    respuesta = True

    respuesta = ((clase_parametros.argumentos.modificaton_date or clase_parametros.argumentos.size
                 or clase_parametros.argumentos.fingerprint)and
                 (clase_parametros.argumentos.dir1 == clase_parametros.argumentos.dir2)and
ñ
                 (validaciones.esdirectorio(clase_parametros.argumentos.dir1)
                 and validaciones.esdirectorio(clase_parametros.argumentos.dir2)
                 and not validaciones.existe_ruta(clase_parametros.argumentos.output)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir1)
                 and validaciones.carpeta_tiene_archivos(clase_parametros.argumentos.dir2)
                 ))
    if respuesta == True:
        print("paso")
    else:
        print("no paso")
    return respuesta



