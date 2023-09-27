import random as rdm

#from macpath import split


abc= "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z" #Nuestro abecedario en string
abc_separado=abc.split() #Creamos un abc que nos sera de utilidad para la creacion de la matriz
bpalabras="MATEMATICAS CIENCIA KEPLER NEWTON SOL ASTROS SUMA RESTA DIVISION FRACCION REPETICION RAIZ CURIE BOHR ALGEBRA LECTURA APRENDER POTENCIA CUADRADO CUBO HIPOTENUSA PARMENIDES PITAGORAS TEOREMA ATOMO MOLECULA ELECTRON PROTON"
bpalabras_separado= bpalabras.split() #Separamos el banco de palabras en una lista
matriz_letras=[] #Aqui se agrgan las letras de manera aleatoria
max_renglon=len(max(bpalabras_separado, key=len)) #Variable que genera el maximo para los renglones dentro de la sopa de letras


#Todas estas variables son variables globales que no seran utiles para la creacion de la sopa de letra

def encontrar_patron(): #Esta funcion busca abrir el archivo excel, leerlo, imprirlo en orden y a partir de ahi generar una serie de preguntas 
    print("----Bienvenido a encontrar al patrón, encuentra el valor de X----")
    juego=open("JuegoPatrones.csv","r") #Aqui abrimos el archivo con su nombre y el read
    respuestas=[] #La lista donde pasaremos todas los renglones del archivo
    for row in juego:
        #print(repr(row))#repr es una funcion interna que despliega los archivos con una vista como de archivo excel
        respuestas.append(row)
    juego.close()#Cerramos el archivo para poder abrir otros archivos

   
    aciertos=0
    jugando=True #La variable que usaremos para finalizar nuestro ciclo while
    while(jugando):
        ej_random=rdm.randint(0,len(respuestas)-1) #GENERAMOS UN indice para un ejercicio random
        ejercicio=respuestas[ej_random].split(",")
        
        longitud_ej_random= len(ejercicio)-2 #Creamos una variable para la longitud del ej random


        indice_incognita=rdm.randint(0,longitud_ej_random-2) #Creamos una indice para la incognita random
        respuesta_incognita=ejercicio[indice_incognita] #Generamos una respuesta dentro de la lista aleatoria con la longitud y el indice
        ejercicio[indice_incognita]="X" #Remplazamos la respuesta por una X
       
        print(ejercicio)
        respuesta_usr=int(input("\nEncuentra el valor de x= "))#Aqui pedimos la respuesta del usuario 


        if(respuesta_usr==int(respuesta_incognita)): #Revisamos que la respuesta del usuario es la misma que la real
            aciertos=aciertos+1
            print("Respuesta correcta", aciertos,"puntos\n")
            if(aciertos==5): #Al momento de tener 5 aciertos seguidos finalizamos
                print("\nFelicidades tuviste 5 aciertos correctos seguidos! Ganaste")
                jugando=False
        else:
            print("\n Tenias", aciertos, "aciertos pero te equivocaste, asi que vuelves a empezar")
            aciertos=0 #Igualamos a 0 el numero de aciertos porque tienen que tener 5 aciertos seguidos
    repetir_juego(encontrar_patron) 


def repetir_juego(modo):#Esta funcion tiene como objetivo el repetir un juego en caso de que algun jugador lo quiera volver a jugar, haciendo uso de parametros
    continuacion=str(input("Deseas seguir jugando este modo SI O NO = ")).lower()#Lo ponemos en .lower() porque es un a manera de evitar errores de dedo
    if(continuacion=="si"):
        modo()#Mandamos el parametro y agregamos parentesis para que se llame como funci
    else:
        print("LLAMAR MENU")


def ahorcado(): #Aqui en el ahorcado se generan todas las variables y listas que nos seran de utilidad para el funcionamiento del juego, ademas de imprimrlo con ciclos para que funcione
    print("\n -------BIENVENIDO A AHORCADOS-------\n")
    palabra=bpalabras_separado[rdm.randint(0,len(bpalabras_separado)-1)].upper()# Genera una palabra dentro del b de palabras random
    nvidas=5 #Es la variable con la cual identificamos el nvidas 
    renglon=[] #Lista donde van renglones
    for letra in range(len(palabra)):#Generamos los renglones del ahorcado
        renglon.append('_') 
    print(" ".join(renglon))
    vivo=True
    while vivo: #Ciclo while que funciona cuando estamos vivos 
        intento=str(input('\nIngresa una letra o palabra=  ').upper())
        if palabra.__contains__(intento or palabra==intento):#Para verificar si tiene la palabra o una letra
            if  palabra==intento:
                print("\n-------Felicidades, es correcto la palabra era------- \n")
                vivo=False #En caso de generarla igualamos vivo a false para finalizar el ciclo while
                repetir_juego(ahorcado) 
                return #Damos este return para terminar con el juego
            
            for letra in range(len(palabra)): #Agui generamos este ciclo para que haga una comparacion letra con letra
                if intento==palabra or intento==palabra[letra]: 
                    renglon[letra]=intento #Vamos generando la lista con la palabra en base a la letra agragada
                    print("\nCORRECTO   VIDAS=", nvidas)
                    print(" ".join(renglon))
                if("".join(renglon)==palabra): #Aqui une la palabra para que sea un solo string y no una lista
                    print("-------Felicidades ganaste, es correcto la palabra era------- \n",palabra)
                    
                    vivo=False #Finalizamos ciclo while
        else:
            nvidas=nvidas-1 #Restamos una vida
            print("INCORRECTO    VIDAS=", nvidas)
            print(" ".join(renglon)) #imprimos el renglon sin cambios
            
            
            if(nvidas==0):
                print("\n-------HAS PERDIDO-------\n")
                vivo=False #finalizamos el juego porque se queddo sin vidas
    repetir_juego(ahorcado)
    return nvidas #Regresamos el nvidas como puntaje

def generarMatriz(): #Esta funcion tiene como objetivo la creacion de una matriz con letras aleatorias y una altura y anchura determinadas
   for columnas in range(max_renglon*2):
        renglon=[]     #Esta variable son donde se iran acumulando todas las letras
        for renglones in range(max_renglon*2):
            renglon.append(abc_separado[rdm.randint(0, len(abc_separado)-1)]) #Aqui hacemos este codigo para que la sopa de letra se vaya generando con letras de nuestra lista
        matriz_letras.append(renglon) #Vamos agregando estos renglones de letras aleatorias
    
def sopaletras(): #Esta funcion es el juego donde ademas mandamos llamar la generacion de matriz y su impresion
    print("\n----BIENVENIDO A LA SOPA DE LETRAS ----\n")
    generarMatriz() #Generamos la matriz de letras aleatorias
    respuestas=[] #Aqui guardaremos todas las respuestas elegidas aleatoriamente de nuestro bando de preguntas
    cpares=0 #Los contadores utiles en los ciclos
    cimpares=0
    npalabras=selec_dificultad()
    for x in range(1,npalabras): #Aqui usamos este for para generar las palabras dentro de nuestra sopa de letras
        palabra=bpalabras_separado[rdm.randint(0,len(bpalabras_separado)-1)] #Generacion de la palabra aleatoria en un rango de 0, a la cantidad de palabras posibles
        lenpalabra=len(palabra) #De utilidad para tener la longitud de la variables y que estas no salgan de nuestro cuadro
        x1y1=[]
        
        #El proceso de agregar palabras se repita con todos los casos siguiendo el mismo proceso que el primero

        if(x%2!=0) : #en esta seccion hacemos las palabras en vertical y horizontal con el contador x que es uno cada de dos
            
            if(cimpares%2==0): #Hacemos uso de cimpares para que sea una horizontal y una vertical
                y1=rdm.randint(0,(max_renglon-1)) #Generamos una coordenada random que no se salga del recuadro para x  y 
                x1=rdm.randint(0,(max_renglon-1-(lenpalabra-1)))

                x1y1.append(x1) #Agregamos esa coordenada a una lista
                x1y1.append(y1)
                for letra in range(lenpalabra):
                    matriz_letras[y1][x1]=palabra[letra] #Dentro de la matriz de letras aleatoria agregamos letra por letra
                    x1=x1+1 #Agregamos +1 al cnontador para generar un nuevo tipo de impresion
            if(cimpares%2!=0):
                palabrareversa=palabra[::-1]
                y1=rdm.randint(0,(max_renglon-1))
                x1=rdm.randint(0,(max_renglon-1-(lenpalabra-1)))

                x1y1.append(x1)
                x1y1.append(y1)
                for letra in range(lenpalabra):
                    matriz_letras[y1][x1]=palabrareversa[letra]
                    x1=x1+1
            cimpares=cimpares+1 #Vamos aumentando el contador para que vaya cambiando el tipo de diagonal o vertical que se imprime
        
        if(x%2==0) :


            if(cpares%2==0): #CODIGO PARA IMPRIMIR EN VERTICAL
                y1=rdm.randint(0,(max_renglon-1-(lenpalabra-1)))
                x1=rdm.randint(0,(max_renglon-1))

                x1y1.append(x1)
                x1y1.append(y1)
                for letra in range(lenpalabra):
                    matriz_letras[y1][x1]=palabra[letra]
                    y1=y1+1

            if(cpares%2!=0): #CODIGO PARA IMPRIMIR EN DIAGONAL
                    y1=rdm.randint(0,(max_renglon-1-(lenpalabra-1)))
                    x1=rdm.randint(0,(max_renglon-1)-(lenpalabra-1))

                    x1y1.append(x1)
                    x1y1.append(y1)
                    for letra in range(lenpalabra):
                        matriz_letras[y1][x1]=palabra[letra]
                        x1=x1+1
                        y1=y1+1
            cpares=cpares+1
        #print(x1y1)
        respuestas.append(palabra)
    nvidas=10 #ASignamos 10 vidas que es la cantidad que queremos
    vivo=True #Usamos nuestra variable vivo para el ciclo while
        
    aciertos=0 #
        
    #print(respuestas)
    print("\n-------AQUI ESTA LA SOPA DE LETRAS, ENCUENTRA 5 PALABRAS, TIENES 10 VIDAS------ \n")
    imprimirMatriz()# Mandamos llamar a la funcion de imprimir matriz para que se vea estructurada y con orden

    while vivo: #Este es nuestro juego
        intento=str(input('\nIngresa una palabra de la sopa de letras=  ').upper()) #tomamos la respuesta en mayuscula para no tener errores de capitalizacion
        if respuestas.__contains__(intento): #En caso de que nuestro intento este dentro de la lista de respuestas ganamos un acierto y se  imprime nuestro n de vidas
            print("\n-------Felicidades, es correcto,  Numero de vidas=",nvidas,"------ \n",)
            aciertos=aciertos+1 #Agregamos a nuestro acumulador
            if(aciertos==5): #En caso de llegar al n de aciertos finalizamos el juego
                print("\n-------Felicidades, es correcto las palabra eran------- \n"," ".join(respuestas))
                vivo=False #Igualamos el vivo a false para que terminel ciclo while
                    
           
        else:
            nvidas=nvidas-1 #en caso de que no coincida restamos una vida 
            print("INCORRECTO,esa palabra no esta, VIDAS= ",nvidas)
        
            
            if(nvidas==0): #cuando el n de vidas es 0 es porque hemos perdido
                print("\n-------HAS PERDIDO-------\n")
                vivo=False #terminamos el ciclo while

    repetir_juego(sopaletras) #Llamamos a la funcion de repetir juego con la sopa de letras



def imprimirMatriz():#En esta funcion aplicamos dos ciclos while para ir imprimiendo la matriz primero renglon y luego por columna
      for z in range(len(matriz_letras)): 
        for a in range(len(matriz_letras[z])):
         print(matriz_letras[z][a], end=" ")
        print("     ",z,"\n")

def selec_dificultad(): #Agui generamos una serie de opciones en cual dependiendo del num que eliga el usuario sera el n de palabras en la sopa de letras
    dificultad=int(input("\n-------BIENVENIDO A LA SOPA DE LETRAS-------\n Elige tu dificultad porfavor \n 1)Facil \n 2) Medio \n 3)Dificil\n "))
    if dificultad==1:
        npalabras=15
    elif dificultad==2:
        npalabras=10
    elif dificultad==3:
        npalabras=8
    elif dificultad>3: #Esto es para que vuelva a llamar la funcion en caso de elegir un num invalido
        print("Elije un num valido")
        sopaletras()
        return
    return npalabras 

def main():
    selecjuego=int(input("Selecciona el modo de juego que desees "))
    #encontrar_patron()
    #ahorcado()
    sopaletras()
    
main()