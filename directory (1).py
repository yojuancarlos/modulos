from functools import wraps
from genericpath import isdir
import core
import file1
from file1 import File

file = file1

class Directory:
    """
    Directory es usado para el manejo de carpetas dentro de los
    procesos de TI.

        :var path: La ruta del directorio dentro del equipo.

        :var regex: Patrón que corresponde o describe (a través
        de campos) la ruta del directorio.

        :var use_full_path: Indica si se usa o devuelve rutas
        absolutas (valor True) o relativas (False).
    """
    def __init__(self, path,path2, regex=r'.*', use_full_path=True):
        self.index = None
        self.path = path
        self.path2= path2
        self.regex = regex
        self.use_full_path = use_full_path
    
    def __iter__(self):
        #if self.use_full_path:
        #    return iter(self.get_file_full_paths())
        #return iter(self.get_file_relative_paths())
        return iter(self.index)
    
    def create_index(self):
        self.index = []
        #aqui modifique
        listaderutas=[self.path,self.path2]
        for rutaactual in listaderutas:
            for root, dirs, files in core.os.walk(rutaactual):
                for f in files:
                    full_path = core.os.path.join(root, f)
                    eval_path = core.re.match(self.regex, full_path)
                    if eval_path is not None:
                        if self.use_full_path:
                            tmp_file = core.File(full_path)
                        else:
                            tmp_file = core.File(full_path, rutaactual)
                        self.index.append(tmp_file)
                        # Imprime las tres partes del File para probar self.use_full_path
                        print(tmp_file)


    @staticmethod
    def create_directory(path:str) -> bool:
        if not core.os.path.isdir(path):
            core.os.makedirs(path)
            return True
        return False
    
    def get_file_full_paths(self) -> list:
        if len(self.index) > 0:
            response = []
            for f in self.index:
                response.append(f.get_full_path())
            return response
        else:
            return []
    
    def get_file_relative_paths(self) -> list:
        if len(self.index) > 0:
            response = []
            for f in self.index:
                response.append(f.get_relative_path())
            return response
        else:
            return []



class claseHijaDeDirectorio(Directory):
    def __init__(self,path,regex,use_full_path):
        super().__init__(self.path, regex=r'.*\.dmx', use_full_path=False)

    def decorador_crear_diccionario(self):

        def funcioninterior(*args, **kwargs):

            diccionario_de_respuesta = {}
            for elemento in self.index:
                archivo = elemento.name  # archivo dmx
                rutabase = elemento.base_path  # ruta base
                ruta = elemento.path  # subcarpetas
                if not archivo in diccionario_de_respuesta:
                    diccionario_de_respuesta[archivo] = {}

                if not rutabase in diccionario_de_respuesta[archivo]:
                    diccionario_de_respuesta[archivo][rutabase] = {}
                    diccionario_de_respuesta[archivo][rutabase]['ruta'] = {}
                # print(diccionario_de_respuesta[archivo][rutabase]['ruta'])

                if not ruta in diccionario_de_respuesta[archivo][rutabase]['ruta']:
                    # diccionario_de_respuesta[archivo][rutabase]['ruta'].append(ruta)
                    diccionario_de_respuesta[archivo][rutabase]['ruta'][ruta] = {}

                for funcionaejecutar in args:
                    diccionario_de_respuesta[archivo][rutabase]['ruta'][ruta][
                        funcionaejecutar.__name__] = funcionaejecutar(elemento.get_full_path())
            print(core.json.dumps(diccionario_de_respuesta, indent=4))

            return funcioninterior


probar=claseHijaDeDirectorio('C:\pruebas\carpeta1','.*\.dmx',False)
probar.decorador_crear_diccionario()



