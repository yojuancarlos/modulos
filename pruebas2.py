def decorator(func):
    def ejecutar(*args, **kwargs):
        print(f"args en ejecutar {args}")
        print(f"kwargs en ejecutar {kwargs}")
        print(ejecutar.__name__)
        func(path=kwargs['ruta'])
    return ejecutar

def tamano(path):
    print(f"tamaño en {path}")

def fecha(path):
    print(f"fecha en {path}")

def sha2(path):
    print(f"sha2 en {path}")

def execute(func, *args,**kwargs):
    print(execute.__name__)
    print(f"args en execute{args}")
    print(f"kwargs en execute{kwargs}")
    tmp=func
    tmp=args
    for f in tmp:
        f(path=kwargs['ruta'])
    return None


cualquercosa=[]
cualquercosa.append(fecha)
cualquercosa.append(tamano)
cualquercosa.append(sha2)
execute(cualquercosa,fecha,tamano,ruta="c:/archivo.txt")
print(30*"---")

ejecu =decorator(tamano)
ejecu2=decorator(sha2)

ejecu(ruta="c:/archivo.txt")
ejecu2(ruta="d:/hola.txt")


...................------------------


def calcular_peso(self):
    lidtapesos = []
    rutabase = self.base_path
    lista = core.os.listdir(rutabase)

    for n in lista:
        peso_archivo_carpeta1 = core.os.path.getsize(set.get_full_path())
        lidtapesos.append(peso_archivo_carpeta1)

    print(f"la lista es de tamaños {lidtapesos}")


def calcular_fechademodificacion(self):
    pass