
resultado=0
ciclo=True
#Suma
def suma(x:float,y:float):
    resultado= x+y+resultado
    print(resultado)
    return resultado

#Resta
def resta(x:float,y:float):
    resultado= x-y
    return resultado

# Multiplicacion
def multi(x:float,y:float):
    resultado= x*y
    return resultado

##Division
def division(x:float,y:float):
    resultado= x/y
    return resultado

# Inicio    
print("Calc:\t Res:",resultado, "\n[+]\t[-]\t[x]\t[/]\t[C]\t[End]\n")
### Ciclo
while ciclo==True:
    
    x=float(input())
    print("\n")
    option=(input())
    print("\n")
    y=float(input())
    print("\n")
    
    print(x)
    print(y)
    print(option)
    
    if option=="+":
        suma(x,y)
        
    if option=="-":
        resta(x,y)
    if option=="x":
        multi(x,y)
    if option=="/":
        division(x,y)
   # if option=="C" | option=="c":
    #    resultado=0
     #   x=0
     #   y=0
   # if option=="End" | option=="end" |option=="END":
    #    ciclo=False
    
    
