#Codigo
def reverse(a):
    b=list(a)
    c=b[::-1]
    r="".join(c)
    return (r)

#Trabajo
a=input("Escribe:")
print("el contrario de" ,a, "es",reverse(a))