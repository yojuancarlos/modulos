import validaciones
import argparse
class parametros :
    opciones = None
    argumentos = None

    def __init__(self):
        self.opciones = argparse.ArgumentParser = argparse.ArgumentParser(description="modulo para filtrar archivos dmx")
        self.opciones.add_argument("--dir1", '-1', required=True, help="directorio uno con archivos dmx")
        self.opciones.add_argument("--dir2", '-2', required=True, help="directorio dos con archivos dmx")
        self.opciones.add_argument("--size", '-s', required=False, action='store_true', help="diferencar archivos dmx por tamaño")
        self.opciones.add_argument("--modificaton_date", "-d", required=False, action='store_true', help="diferenciar archivos dmx por fecha de modificacion")
        self.opciones.add_argument("--fingerprint", "-f", required=False, action='store_true', help="diferenciar archivos dmx por figerprint")
        self.opciones.add_argument("--output", "-o", required=True, help="ruta del archivo json que se va a crear con los resultaods")



    def validar(self):
        respuesta=True
        self.argumentos = self.opciones.parse_args()

        respuesta= (self.argumentos.modificaton_date or self.argumentos.size or self.argumentos.fingerprint)\
                and validaciones.esdirectorio(self.argumentos.dir1) \
                and validaciones.esdirectorio(self.argumentos.dir2) \
                and validaciones.directorio_existe(self.argumentos.output) \
                and validaciones.directorios_iguales(self.argumentos.dir1,self.argumentos.dir2)

        return respuesta

        # function to print both directories
    def print_args(self):
        if self.validar():
            directory1 = self.argumentos.dir1
            directory2 = self.argumentos.dir2
            salida = self.argumentos.output
            print(f'Directorio 1: {directory1}  Directorio 2: {directory2}  salida {salida}')
        else:
            print("self.validar()")




