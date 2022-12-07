#funcion suma
def slista(a):
    sumatorio=0
    for i in a:
        sumatorio+=i
    return sumatorio

#funcion multiplicación
def mlista(b):
    multiplicatorio=1
    for i in b:
        multiplicatorio*=i
    return multiplicatorio

#Tarea
c=[2,4,6,8,10,12,14,16,18,20]
print ("la suma de todos los numeros es:",slista(c))
print ("y en multiplicación es:",mlista(c))