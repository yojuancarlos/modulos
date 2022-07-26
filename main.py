import parametros
import unificar
import validaciones


def main():
    argumento = parametros.Parametros()
    argumento.parseo()

    if valida(argumento):
        app = unificar.AppUnificarDMX(argumento.argumentos.dir1,argumento.argumentos.dir2,
            argumento.argumentos.output,argumento.argumentos.size,
            argumento.argumentos.modificaton_date,argumento.argumentos.fingerprint)


def valida(parametros:parametros.Parametros):
    tiene_opciones = parametros.argumentos.modificaton_date \
                or parametros.argumentos.size \
                or parametros.argumentos.fingerprint
    dir_diferentes = parametros.argumentos.dir1 != parametros.argumentos.dir2
    valida_argumentos = validaciones.esdirectorio(parametros.argumentos.dir1) \
                and validaciones.esdirectorio(parametros.argumentos.dir2) \
                and not validaciones.existe_ruta(parametros.argumentos.output) \
                and validaciones.carpeta_tiene_archivos(parametros.argumentos.dir1) \
                and validaciones.carpeta_tiene_archivos(parametros.argumentos.dir2)
    '''print(f'{validaciones.esdirectorio(parametros.argumentos.dir1)} '
          f'{validaciones.esdirectorio(parametros.argumentos.dir2)} '
          f'{not validaciones.existe_ruta(parametros.argumentos.output)} '
          f'{validaciones.carpeta_tiene_archivos(parametros.argumentos.dir1)} '
          f'{validaciones.carpeta_tiene_archivos(parametros.argumentos.dir2)}')
    print(f'{tiene_opciones} , {dir_diferentes} , {valida_argumentos}')'''
    respuesta = tiene_opciones and dir_diferentes and valida_argumentos

    print(f'respuesta de valida argumentos {respuesta}')
    '''
    if respuesta:
        print("paso")
    else:
        print("no paso")
    '''
    return respuesta


if __name__ == '__main__':
    main()
