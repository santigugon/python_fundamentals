import pandas as pd

new_list = [["first", "second","third"], ["third", "four"], ["five", "six"]]
df = pd.DataFrame(new_list)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()

texto="hola"
texto=list(texto)
print(texto)


f=open("answers2.csv","r")#Abrimos el archivo con la funcion interna, ponemos el modo r que represnta que vamos a abrir el modo lectura
respuestas=[]
for row in f:
    print(repr(row))#repr es una funcion interna que despliega los archivos con una vista como de archivo excel
    respuestas.append(row)
f.close()#Cerramos el archivo para poder abrir otros archivos
answers=[]
for recorre in respuestas:
    answers.append(recorre.strip().split(" "))
print(answers)

 for z in range(len(matriz_letras)): 
        for a in range(len(matriz_letras[z])):
         print(matriz_letras[z][a], end=" ")
        print("     ",z,"\n")

