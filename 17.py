#funcion reverse
def reverse(a):
    b=list(a)
    c=b[::-1]
    r="".join(c)
    return (r)
#funcion palindromo
def palindromo(a):
    c=reverse(a)
    x=0
    for i in range(len(a)):
        if a[i]!=c[i]:
            x+=1
    if x!=0:
        return False
    else:
        return True

#Tareas
ñ=input("Escribe una palabra:")
if palindromo(ñ):
    print("La palabra" ,ñ, "Al reves es" ,reverse(ñ), "y suena igual que del reves")
else:
    print(ñ, "al reves es" ,reverse(ñ), "y NO suena igual")