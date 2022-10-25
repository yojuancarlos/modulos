def peso():
    a="aaa"

    return a
def tamano():
    b="bbb"
    return b
def fecha():
    c="ccc"
    return c
def funcion(*args):

    for f in args:
        print(args)
        print(f"la funcion que usted uso es {f()} y su npombre es {f.__name__}")


funcion(peso)