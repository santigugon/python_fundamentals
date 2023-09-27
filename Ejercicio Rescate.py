#A00572499
#Santiago Gutierrez Gonzalez
#Ejercicio Rescate
import math as m
def main():
    n=int(input("Ingresa n= "))
    m=int(input("Ingresa m= "))
    x=0
    for a in range(m):
        x=x+1/(n+a+1)
        
    x=round(x,2)
    print(x)

main()