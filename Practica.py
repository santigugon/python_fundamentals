def crear_matriz(renglones,columnas):
    matriz=[]
    for renglones in range(renglones):
        renglon=[]
        print(columnas)  
        for x in range(0,columnas):
            print("Ingresa el dato en la posicion semana", renglones+1,"venta", x+1)
            nuevo_dato=input("=")
            renglon.append(nuevo_dato)
        matriz.append(renglon)
    
    return matriz

def estadisticas(matriz):
    resultados=[]
    multi_diag=1
    for x in range(len(matriz)):
        multi_diag=multi_diag*int(matriz[x][x])
    print("\nLa multiplicacion diagonal es igual a ",multi_diag)
    contador=0
    resultados.append(multi_diag)
    columnaslista=[]

    for renglon in range(len(matriz)):
        s_column=0
        for columna in range(len(matriz[renglon])):
            s_column=s_column+int(matriz[columna][renglon])
            contador=contador+1
        resultados.append(s_column)
        columnaslista.append(s_column)
    
    maximg=0
    minimg=int(matriz[0][0])

    for a in range(len(matriz)):
        maximl=int(max(matriz[a]))
        miniml=int(max(matriz[a]))
        if(maximl>maximg):
            maximg=maximl
        if(miniml<minimg):
            minimg=miniml
            


      
  

    print("\nLa suma de columnas es", columnaslista)
    promedio_reng=s_column/contador
    listaresumen=[]
    #(SUMA DIAGONAL, SUMA COLUMNA1, SUMACOLUMNA2)
    print("\nEl promedio de la suma de columnas es",sum(columnaslista)/len(columnaslista))
    print("El maximo dentro de las columnas es",maximg)
    print("El minimo dentro de las columnas es", minimg)

    return resultados
        


def main():
    print("\nBienvenido al Sistema de ventas, a continuación ingresa los datos que se te piden \n")
    nsemanas=int(input("Ingresa por favor el numero de semanas de venta= "))
    ncolumnas=int(input("Ingresa el numero de articulos esa semana= "))
    if(nsemanas>0 and ncolumnas>0 and ncolumnas==nsemanas):
        matriz=crear_matriz(nsemanas,ncolumnas)
        
    
        for z in range(len(matriz)): 
            for a in range(len(matriz[z])):
                print(matriz[z][a], end=" ")
            print("  ","Semana",z+1,"\n")
        listaEst=estadisticas(matriz)
    else:
        print("\n!!!!!!!!!!!!!!!!Ingresa un numero valido!!!!!!!!!!!!!!!!\n")
        main() 

   


main()