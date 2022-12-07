def gran(e,z):
    a=z
    if (z>e):
        print(z,"es mayor que" ,e)
    elif (e>z):
        a=e
    else:
        print(e,"y" ,z, "son lo mismo")
    return a

e= input("escribe un numero:")
z= input("escribe otro numero:")
c= gran(e,z)
print ("el mas grande entre",z, "y" ,e, "es el" ,c)