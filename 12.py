def gran (a,b,c):
    if (a>b):
        if (a>c):
            e=a
        elif(a<c):
            e=c
        else:
            e=a
    elif (a<b):
        if(a>c):
            e=b
        elif(a<c):
            e=c
        else:
            e=b
    else:
        if(a>c):
            e=a
        elif(a<c):
            e=c
        else:
            e=a
    return e

a=input("Pon un numero:")
b=input("Pon otro numero:")
c=input("Pon OTRO numero:")
d=gran (a,b,c)
print ("el mas grande entre",a, "y" ,b, "y" ,c, "son" ,d)