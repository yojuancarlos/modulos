import parametros
import unificar
def main():
    bandera = parametros.Parametros()
    bandera.parseo()
    unificar.valida(bandera)

if __name__ == '__main__':
    main()
