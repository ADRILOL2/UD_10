#funcion suma
def slista(a):
    sumatorio=0
    for i in a:
        sumatorio= sumatorio + (i*i)
    return sumatorio
#funcion multiplicación
def mlista(b):
    multiplicacion=1
    for i in b:
        multiplicacion*=multiplicacion * (i*i)
    return multiplicacion

#Tarea
c=[3,5]
print ("la suma de todos los numeros es:",slista(c))
print ("y en multiplicación es:",mlista(c))