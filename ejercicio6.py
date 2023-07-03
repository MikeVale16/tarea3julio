# Escribe una función que genere una lista con los números de la serie de fibonacci. La función debe recibir la cantidad de números a generar


def fibonnaci(num):
    num1=0
    num2=1
    resultado=0
    print(num1)
    for i in range(0,num):
    
        resultado=num1+num2
        print(resultado)
        num1=num2
        num2=resultado
    return "Success"

iteration= int(input("Por favor dime cuantos elementos de fibonacci quieres ver?\n"))
print("\n\n\n\n\n")

print(fibonnaci(iteration))
