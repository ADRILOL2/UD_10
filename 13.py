#funcion
def longitud(a):
    contador=0
    for i in a:
        contador+=1
    return contador

#Programa
b=[1,"a",[3,4],5,6]
print (longitud (b))