import core

class File:
    """
    File es usado para el manejo de archivos dentro de los procesos de IT
        
        :var fingerprint: Es de tipo dicitionary donde key corresponde
        al tiempo en que se tomó y con el formato yyyy-mm-ddTHH:MM:ss
        ó la palabra latest. El value corresponde a RSHA calculado

        :var name: Nombre completo del archivo, con extensión.

        :var path: Ruta completa al archivo. Si se indica base_path en
        el constructor, se determina la ruta como una relativa y se
        almacena base_path para crear una ruta completa.
    """

    def __init__(self, path:str, base_path:str = None):
        self.dict_fingerprint = {}

        if base_path is None:
            self.base_path, self.name = core.os.path.split(path)
            self.path = ''
        else:
            self.path, self.name = core.os.path.split(core.os.path.relpath(path, base_path))
            self.base_path = base_path
    
    def __str__(self):
        response = f'({self.base_path})({self.path})({self.name})'
        return response

    @staticmethod
    def calculate_fingerprint(path):
        """"
        Función que determina un hexadecimal con el código hash SHA1 de un archivo. No
        lee paquete de más de 1024 bytes.

            :return: Cadena de texto con la representación en hexadecimal del SHA1 calculado
        """
        h = core.hashlib.sha1()
        if path is None:
            raise Exception('Sin ruta para calcular fingerprint')
        else:
            file_to_read = path

        with open(file_to_read, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        str_value = h.hexdigest()
        return str_value

    @staticmethod
    def calcular_peso(path):
        """"
            Función que determina el peso de un archivo el cual es entregado en bytes.

            :return: peso de un archivo
                       """
        if path is None:
            raise Exception("la ruta no es valida,por favor introdusca una ruta valida")
        else:
            peso_archivo = core.os.path.getsize(path)
        return peso_archivo
    @staticmethod
    def calcular_fechademodificacion(path):
        """"
                Función que determina la ultima fecha de modificacion de un  archivo.

                    :return: ultima fecha de modificacion de un archivo.
                """

        if path is None:
            raise Exception("la ruta no es valida,por favor introdusca una ruta valida")
        else:
            ti_m = core.os.path.getmtime(path)
            fecham = core.time.ctime(ti_m)

        return fecham
    def get_full_path(self):
        """

            :return: Tuple with parts of the full path
        """
        return core.os.path.join(self.base_path, self.path, self.name)
    
    def get_relative_path(self):
        """

            :return: Tuple with parts of the relative path
        """
        return core.os.path.join(self.path, self.name)

    def split_name(self, string=None, separator=' '):
        """
        Separa una cadena (llamada string) en campos con un separador

            :param string: La cadena de texto a separar
        
            :param separator: Los caracteres que se van a usar como separador.
            Por defecto es un espacio en blanco( ).
            
            :return: ¿¿¿¿¿???????????. Si falla retorna None.
        """
        pass
        return None

    def new_name(self, new_name=None):
        """
        Indica un nuevo nombre al archivo.
            :param new_name: El nuevo nombre del archivo debe ser completo e
            incluir la extensión.

            :return: Un True si cambió el nombre
        """
        self.name = new_name
        return True
    
    def change_extension(self, new_extension:str) -> str :
        tmp_name, tmp_ext = core.os.path.splitext(self.name)
        tmp = new_extension.lower()
        return f'{tmp_name}.{tmp}'
    
