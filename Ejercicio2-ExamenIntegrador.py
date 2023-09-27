#A00572499
#Santiago Gutierrez Gonzalez

def lecturaExcel():

    f=open("RegistroVentasExamen.csv","r")#Abrimos el archivo con la funcion interna, ponemos el modo r que represnta que vamos a abrir el modo lectura
    renglones=[]
    for row in f:
        renglones.append(row)
    f.close()#Cerramos el archivo para poder abrir otros archivos
    matriz=[]
    for recorre in renglones:
        matriz.append(recorre.strip().split(" "))

    for z in range(len(matriz)): 
        for a in range(len(matriz[z])):
            print(matriz[z][a], end=" ")
        print("     ","Semana",z,"\n")
    matriz_separada=[]
    for x in range(len(matriz)):

        renglon=matriz[x][0].split(",")
        renglonint=[]
        for y in range(len(renglon)):
            nint=int(renglon[y])
            renglonint.append(nint)
            
        matriz_separada.append(renglonint)
        

    return matriz_separada


def estadisticas(matriz):
    resultados=[]
    multi_diag=1
    for x in range(len(matriz)):
        multi_diag=multi_diag*int(matriz[x][x])
    print("\nLa multiplicacion diagonal es igual a ",multi_diag)
    contador=0
    resultados.append("Multiplicacion diagonal=")
    resultados.append(multi_diag)
    resultados.append("Suma de columas=")
    columnaslista=[]

    for renglon in range(len(matriz)):
        s_column=0
        for columna in range(len(matriz[renglon])):
            s_column=s_column+int(matriz[columna][renglon])
            contador=contador+1
        resultados.append(s_column)
        columnaslista.append(s_column)
      
  

    print("\nLa suma de columnas es", columnaslista)
    promedio_reng=s_column/contador
    listaresumen=[]
    #(SUMA DIAGONAL, SUMA COLUMNA1, SUMACOLUMNA2)
    maximg=0
    minimg=matriz[0][0]
    for a in range(len(matriz)):
        maximl=int(max(matriz[a]))
        miniml=int(max(matriz[a]))
    
        if(maximl>maximg):
            maximg=maximl
        if(miniml<minimg):
            minimg=miniml
    resultados.append("Maximo")
    resultados.append(maximg)
    resultados.append("Minimo")
    resultados.append(minimg)
    resultados.append("Promedio columnas")
    resultados.append(sum(columnaslista)/len(columnaslista))



    import pandas as pd

    
    df = pd.DataFrame(resultados)
    writer = pd.ExcelWriter('resultadosEx.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()


    return resultados

def main():
    matriz=lecturaExcel()
    estadisticas(matriz)


main()