#Escribe un programa que pueda identificar si una palabra o frase es un palíndromo (https://es.wikipedia.org/wiki/Pal%C3%ADndromo).

def palindromo(String):
    inicio = 0
    fin = len(String) - 1

    while String[inicio] == String[fin]:
     
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

cadena= input("Dame la cadena a analizar: \n")
cadena_limpia=cadena.replace(" ","")
print(cadena_limpia)
palindromo(cadena_limpia)
print(palindromo(cadena_limpia))