#funcion
def crear_repetidos(a,b):
    #a=numero
    #b=caracteres a repetir
    c=b*int(a)
    return c
#Tarea
c=input ("Pon un numero:")
d=input ("pon caracteres a repetir por el numero:")
print("el caracter" ,d, "repetido" ,c, "vezes son:" ,crear_repetidos(c,d))
