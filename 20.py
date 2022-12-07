#funcion
def crear_repetidos(a,b):
    c=b*int(a)
    return c

def crear_puntos(a):
    for e in a:
        c=crear_repetidos(int(e),".")
        print(c)

a=input("Crea lista de nueros sin comas:")
crear_puntos(a)