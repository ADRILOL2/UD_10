a=input ("¿Como te llamas?\n")
b=input ("¿Cuantos años tienes? \n")
if (int(b)>18):
    print("te llamas",a, "y eres mayor de edad")
elif (int(b)<18):
    print("te llamas" ,a, "y eres menor de edad")
else:
    print("te llamas" ,a, "y tienes" ,b, "años")