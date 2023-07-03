#Escribe una función que permita multiplicar varios números

def multiplicame(*args):
    result=1  ### Aqui cambialo por 1

    for i in args:
        result *= i
    return result

resultado=multiplicame(8,9,34,86,9)
print("la multiplicacion de todo es: ",resultado)
