# Importamos funcion ArgumentParser
import os
import argparse
import sys





def directorio_existe(directory):
    return not os.path.exists(directory)


def esdirectorio(directory):
#si es directorio me retorna true sino lo es retorna false
    return os.path.isdir(directory)

def esarchivo(directory):
# si es archivo me retorna true sino lo es retorna false
    return os.path.isfile(directory)

def directorios_iguales(directorio1, directorio2):
    return not directorio1 == directorio2
