import os
import validaciones
import argparse
import sys
import parametros
def main():
    parameters=parametros.parametros()
    parameters.validar()
    parameters.print_args()
if __name__ == '__main__':
    main()
