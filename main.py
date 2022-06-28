import os
import modulos
import argparse
import sys

def main():
    # Definicion de los argumentos
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="algo despues lo mejoro")
    parser.add_argument("--dir1", '-1', required=True, help="directorio uno con archivos dmx")
    parser.add_argument("--dir2", '-2', required=True, help="directorio dos con archivos dmx")
    parser.add_argument("--size", '-s', required=False,action='store_true', help="diferencar archivos dmx por tamaño")
    parser.add_argument("--modificaton_date", "-d",required=False,action='store_true', help="diferenciar archivos dmx por fecha de modificacion")
    parser.add_argument("--fingerprint", "-f", required=False,action='store_true', help="diferenciar archivos dmx por figerprint")
    parser.add_argument("--output", "-o", required=True, help="ruta del archivo json que se va a crear con los resultaods")
    # Parseo de los argumentos
    args = parser.parse_args()

    #call function print_args
    print_args(args)

# function to print both directories
def print_args(args):
   modulos.validate_args(args)
   directory1 = args.dir1
   directory2 = args.dir2
   salida= args.output
   print(f'Directorio 1: {directory1}  Directorio 2: {directory2}  salida {salida}')

if __name__ == '__main__':
    main()
