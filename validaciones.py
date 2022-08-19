import os
"este es un scrip encargado de contener todas las validaciones que puedan ser reutilizados en proyectos que incluyan directorios"
def existe_ruta(directorio):
    return  os.path.exists(directorio)

def esdirectorio(directorio):
#si es directorio me retorna true sino lo es retorna false
    return os.path.isdir(directorio)

def esarchivo(directorio):
# si es archivo me retorna true sino lo es retorna false
    return os.path.isfile(directorio)

def carpeta_tiene_archivos(directorio):
    if os.listdir(directorio):
        return True
    else:
        return False
