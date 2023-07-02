# 1 Escribe una función qué reciba varios números y devuelva el mayor de ellos
def mayor_num():
    num_amount= int(input("Por favor indicame cuantos numeros quieres ingresar?\n"))
    mayor=0   

    for i in range(num_amount):
        num=int(input("Por favor ingresa un numero\n"))
        if  num>mayor:
            mayor=num
    return mayor        

resultado=mayor_num()

print("El mayot numero es: ",resultado)


             
