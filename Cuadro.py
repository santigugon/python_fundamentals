import random as rdm

def cuadro():
  resultado=rdm.randint(10,20)#Crea resulta num magico entre 10 y 15
  cuadroNOMagico=True #Variable para que corra el while
  print(resultado)
  
  while(cuadroNOMagico):
    linea1=[]
    linea2=[]
    linea3=[]
    for x in range(3):
      num1=rdm.randint(1,10)
      linea1.append(num1)
      num2=rdm.randint(1,10)
      linea2.append(num2)
      num3=rdm.randint(1,10)
      linea3.append(num3)
      
    if sum(linea1)==resultado and sum(linea2)==resultado and sum(linea3)==resultado and linea1[0]+linea2[0]+linea3[0]==resultado and linea1[1]+linea2[1]+linea3[1]==resultado and linea1[2]+linea2[2]+linea3[2]==resultado and linea1[0]+linea2[1]+linea3[2]==resultado:
      print(linea1)
      print(linea2)
      print(linea3)
      cuadroNOMagico=False
      
  cuadro()