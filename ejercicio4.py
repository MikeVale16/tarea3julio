#Escribe una función que permita identificar si un número dado es primo o no.

def primo(x):
    if x%2!=0:
        print(x," es primo\n\n\n\n")
    else:
        print(x," no es primo\n\n\n\n")

print("-------------Conozcamos si un numero es primo o no------")
continuar=True

while continuar==True:
    opcion=int(input("Dame una opcion por favor:\n1)Conocer si un numero es primo\n2)Salir\n"))
    
    if opcion==1:
        x=int(input("Dame un numero\n"))
        primo(x)
    if opcion==2:
        continuar=False
        
    
