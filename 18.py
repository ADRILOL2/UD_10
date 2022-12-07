

#funcion superposición
def superposición(a, b):
    n=0
    for e in a:
        n +=b.count(e)
    if n>0:
        return [n,True]
    else:
        return [0,False]

#Tarea
a=input("Escribe una lista:")
b=input("Escribe otra lista:")
c,d=superposición(a,b)
if (c==0):
    print("las 2 listas no tienen nada en comun")
else:
    print("las 2 listas tienen" ,c, "cosas en comun")