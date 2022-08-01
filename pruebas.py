import os


def decorador(func):
    def wrapper(*args, **kwargs):
        # func(*args, **kwargs)
        archivos = kwargs['lista']
        ruta = kwargs['ruta']
        for archivo in archivos:
            ruta_completa = os.path.join(ruta, archivo)
            print(f'>> {ruta_completa}')
            for funcion in args:
                archivos[archivo][funcion] = f'valor calculado con {funcion}'
                if 'error' in archivos[archivo]:
                    archivos[archivo]['error'] += ' | mensaje de error'
                else:
                    archivos[archivo]['error'] = 'mensaje de error'

        return archivos

    return wrapper


def vacia(*args, **kwargs):
    pass


def listar_directorio(ruta: str) -> dict:
    respuesta = {}
    respuesta[ruta] = {}
    # lista = os.listdir(ruta)
    lista = ['ar1', 'ar2', 'ar3']
    for item in lista:
        respuesta[ruta][item] = {}
    return respuesta


def dict_a_set(dict_ruta: dict) -> set:
    respuesta = set()
    for item in dict_ruta:
        respuesta.add(item)
    return respuesta


dir1 = ['ar1', 'ar2', 'ar3']
dir2 = ['ar3', 'ar4', 'ar5', 'ar6']

ruta_dir1 = 'c:/ruta/dir1'
ruta_dir2 = 'c:/ruta/dir2'
dict_dir1 = listar_directorio(ruta_dir1)
print(dict_dir1)
conj_dir1 = dict_a_set(dict_dir1[ruta_dir1])
print(conj_dir1)
# conj_dir1=set(dir1)
# conj_dir2=set(dir2)
# print(conj_dir1 & conj_dir2)

indexar_dir = decorador(vacia)
print(indexar_dir('tamano', 'size', lista=dict_dir1[ruta_dir1], ruta=ruta_dir1))
print(dict_dir1)
# indexar_dir(lista=dir2)

for dir in dict_dir1:
    for arch in dict_dir1[dir]:
        if 'error' in dict_dir1[dir][arch]:
            lista_errores = dict_dir1[dir][arch]['error'].split('|')
            print(lista_errores)



"""""
preguntas 


if __name__ =="_main"
    
    
kwargs----------------------->llave=valor 
metodo  usando called

metodos especiales


tutorial yleld python
"""""