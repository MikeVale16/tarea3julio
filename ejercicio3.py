#Escribe una función para verificar que un número se encuentra en un rango de números determinado. El resultado de esa función debe ser booleano
test=False
def mayor(*args):
    total=0
    for i in args:
        #num=int(input("Dame un numero"))
        if i>total:
            total=i
    return total

def menor(*args):
    total2=99999999
    for i in args:
        #num=int(input("Dame un numero"))
        if i<total2:
            total2=i
    return total2

prueba= mayor(8,9,22,14)
prueba2= menor(8,9,22,14)
print("El numero mas alto es: ",prueba)
print("El numero menor es: ",prueba2)

n=int(input("Dame un numero: \n"))
if n>prueba2 and n<prueba: 
    test=True
    print(test)
    
else:
    print(test)
    
