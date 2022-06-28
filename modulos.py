# Importamos funcion ArgumentParser
import os
import argparse
import sys

def validate_args(args):
    directory1 = args.dir1
    directory2 = args.dir2
    # validadaciones
    if os.path.isdir(directory1) == False:
        resultado = print("la carpeta 1 no existe por favor escriba un diretorio valido")
        sys.exit(1)
    elif os.path.isdir(directory2) == False:
        resultado = print("la carpeta 2 no existe por favor escriba un directorio valido")
        sys.exit(1)
    elif args.dir1 == args.dir2:
        resultado = print("ambas carpetas son iguales por favor escriba dos carpetas distintas ")
        sys.exit(1)