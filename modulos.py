# Importamos funcion ArgumentParser
import os
import argparse
import sys

def validate_args(args):
    output= args.output
    # validadaciones
    if not isdir(args.dir1):
        resultado = print("la carpeta 1 no existe por favor escriba un diretorio valido")
        sys.exit(1)
    elif not isdir(args.dir2):
        resultado = print("la carpeta 2 no existe por favor escriba un directorio valido")
        sys.exit(1)
    elif args.dir1 == args.dir2:
        resultado = print("ambas carpetas son iguales por favor escriba dos carpetas distintas ")
        sys.exit(1)
    elif isfile(output) and  not isdir(output):
        resultado = print("la ruta de entrada es invalida")
        sys.exit(1)
    elif not (args.modificaton_date or args.size or args.fingerprint):
        print('elija el proceso que quiera realizar')
        sys.exit(1)


def isfile(directory):
    return os.path.isfile(directory)

def isdir(directory):
    return os.path.isdir(directory)