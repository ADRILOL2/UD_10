#funcio
def vocal(a):
    if (a=="a" or a=="A" or a=="e" or a=="E" or a=="i" or a=="I"  or a=="o" or a=="O"  or a=="u" or a=="U"):
        return True
    else:
        return False

#tarea
a=input("escribe una letra del abecedario:")
print("Indica si es una vocal o no \n si es vocal:True \n si no lo es:False \n",vocal(a))