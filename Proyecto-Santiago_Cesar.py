# -*- coding: utf-8 -*-
#SANTAGO GUTIERREZ GONZALEZ
#CESARSANCHEZ
"""
Menu
"""
import webbrowser #Esta es nuesta libreria investigada que nos permite acceder a un link de internet directamente, con el cual podemos ver nuestro juego, su inventario o todo lo que hay que saber
import random as rdm
import random as ran #importamos la biblioteca random

puntaje=[]
#_____________________________________SUMA Y RESTA FUNCIONES_______________________________
def matriz_rand1(x,y): #definimos la funcion
    l=[] #Lista vacia para hacerla matriz
    for a in range(x): #comenzamos con el rango de aplitud de los renglones
        l2=[] #lista vacia para luego agregarla a la variable l
        for b in range(x): # Luego el rango de aplitud de las columnas
            l2.append(ran.randrange(1,y)) #agregamos a una lista los randoms
        l.append(l2) #juntamos la anterior lista a la lista de la matriz
    for c in l:
        print(c) #leemos la matriz
    print('')
    return l #regresamos la matriz con randoms
        

def suma_f(m1,m2): #definimos funcion de suma de matrices
    suma=[] # definimos suma como lista, pues sera nuestra variable final para la matriz
    fila=0 # nos ayudara a identificar las cordenadas dentro de las otras matrices
    for renglon in m1: #vamos leyendo la matriz 1
        lista=[]#es una lista que sera agregada a otra lista
        columna=0# nos ayuda como la variable fila
        for n in renglon: #seguimos leyendo la matriz q
            r=n+m2[fila][columna] #usamos los datos para sumar y ponerlo a la variable r
            
            lista.append(r) #Añadimos r a la otra matriz
            columna=columna+1
        fila=fila+1
        suma.append(lista) #Añadimos la lista a la otra matriz
    return suma #regresamos la matriz sumada

def resta_f(m1,m2): #definimos funcion
    resta=[] #variable para la matriz final
    fila=0 # variable para identificar coordenadas
    for renglon in m1: #vamos leyendo la matriz 1
        lista=[] #se va a guardar el 
        columna=0 # me sirve para identificar coordenadas
        for n in renglon: #seguimos leyendo la matriz 1
            r=n-m2[fila][columna] #usamos los datos para restar y ponerlo a la variable r
            
            lista.append(r) #añadimos a una lista
            columna=columna+1
        fila=fila+1
        resta.append(lista)#añadimos la lista a otra para crear una matriz
    return resta #Return porque siempre son buenos
    
    
def suma_resta():  #funcion para suma y resta de matrices, donde se usan las funciones de llenado de matrices, resta de matrices y suma de estas
    print('- - - Iniciando juego de suma y resta - - -\n')
    
    dificultad=int(input('¿Que nivel quieres 1, 2 o 3?')) #definimos dificultad
    print('Intrucciones: Apareceran 2 cuadrantes, elige un cuadrante y suma o resta cada valor con el correspondiente dentro del otro cuadrante ')
    #
    if dificultad==1: # if para identificar niveles de dificultad seleccionados
        puntuacion=0 #Definimos variables que se usaran
        fila=0
        columna=0
        matriz1=matriz_rand1(3,10)
        matriz2=matriz_rand1(3,10) #guardamos dos diferentes matrices y las leemos
        matriz_s=suma_f(matriz1,matriz2) 
        matriz_r=resta_f(matriz1,matriz2)#guardamos tanto la resta como la  suma de dichas matrices en otras dos variables
        for x in matriz_s:
            columna=0
            for y in x:
                random=ran.randrange(1,11) # definimos una variable random para luego determinar si sera suma o resta
                if random%2==1: # con esto vemos si vamos a restar o sumar
                    resp=int(input('Suma de los puntos (' + str(columna + 1) + ',' + str(fila*-1 + 3) + '): '))
                    columna=columna+1
                    if resp==y: #checamos si el resultado es correcto
                        puntuacion=puntuacion+1
                else:
                    resp=int(input('Resta de los puntos (' + str(columna + 1) + ',' + str(fila*-1 +3 ) + '): '))
                    
                    
                    if resp==matriz_r[fila][columna]: #Usamos la matriz de resta para conocer el valor de la resta y aplicar un if
                        puntuacion=puntuacion+1 #Sumamos un punto a la variable que contiene la puntuacion
                    columna=columna+1
                
            fila=fila+1
        print(str(puntuacion)+ '/9') # Imprimimos la puntuacion junto con los posibles resultados
        return ['Suma y resta dif 1', puntuacion] #Mandamos el resultado en una lista, para el sistema de historial y puntuacion
    
        #Se repite el proceso de lo anterior pero ahora con valores de random mas altos, por lo tanto mas dificil
        
        
    if dificultad==2:
        puntuacion=0
        fila=0
        columna=0
        matriz1=matriz_rand1(3,100)
        matriz2=matriz_rand1(3,100)
        matriz_s=suma_f(matriz1,matriz2)
        for x in matriz_s:
            columna=0
            for y in x:
                random=ran.randrange(1,11)
                if random%2==1:
                    resp=int(input('Suma de los puntos (' + str(columna + 1) + ',' + str(fila*-1 + 3) + '): '))
                    columna=columna+1
                    if resp==y:
                        puntuacion=puntuacion+1
                else:
                    resp=int(input('Resta de los puntos (' + str(columna + 1) + ',' + str(fila*-1 +3 ) + '): '))
                    
                    
                    if resp==matriz_r[fila][columna]:
                        puntuacion=puntuacion+1
                    columna=columna+1
            fila=fila+1
        print(str(puntuacion)+ '/9')
        return ['Suma y resta dif 2', puntuacion]
        
    #De nuevo volvemos a repetir todo lo hecho anteriormente
    if dificultad==3:
        puntuacion=0
        fila=0
        columna=0
        matriz1=matriz_rand1(5,100)
        matriz2=matriz_rand1(5,100)
        matriz_s=suma_f(matriz1,matriz2)
        for x in matriz_s:
            columna=0
            for y in x:
                random=ran.randrange(1,11)
                if random%2==1:
                    resp=int(input('Suma de los puntos (' + str(columna + 1) + ',' + str(fila*-1 + 3) + '): '))
                    columna=columna+1
                    if resp==y:
                        puntuacion=puntuacion+1
                else:
                    resp=int(input('Resta de los puntos (' + str(columna + 1) + ',' + str(fila*-1 +3 ) + '): '))
                    
                    
                    if resp==matriz_r[fila][columna]:
                        puntuacion=puntuacion+1
                    columna=columna+1
            fila=fila+1
        print(str(puntuacion) + '/25')
        repetir_juego(suma_resta)
        return ['Suma y resta dif 3', puntuacion]
        
        
        

    
    
#_____________________________________FIN SUMA Y RESTA FUNCIONES__________________________________

#_____________________________________ SUMA Y RESTA FRACCIONES__________________________________
def sum_fracc(): #Definimos una funcion para el juego de suma y resta de fracciones
    puntuacion=0
    print('- - - Iniciando juego de suma y resta fracciones - - -\n')
    dificultad=int(input('¿Que nivel quieres 1, 2 o 3?')) #preguntamos la dif y la guardamos en variable
    
    for v in range(5): #se realizara 5 veces, por eso el for
        random=ran.randrange(1,10)
        result=fracc(random,v,dificultad) #se envia a la funcion de fracc para imprimir las fracciones y mandar el resultado de su resta o suma
        #se envia con el numero random que servira para saber si va a ser suma o resta,  tambien se envia con v para determinar el numero de ejercicio
        #por ultimo se envia con la dificultad del mismo
        numerador=int(input('Numerador: ')) #preguntamos el numerador del resultado
        denominador=int(input('Denominador: ')) #preguntamos el denominador del resultado
        
        if numerador/denominador==result: #checamos si esta bien
            print('Acertaste')
            puntuacion=puntuacion+1 #variable acumuladora para contar los puntos
        else:
            print('Mal resultado\n') #Si no esta bien, ponemos ese mensaje
    print(puntuacion,'/5')
    print('- - - Saliendo juego de suma y resta fracciones - - -\n')
    repetir_juego(sum_fracc)
    return ['Suma y resta fracc dif ' + str(dificultad), puntuacion] #Enviamos al menu el resultado para el historial y el registro de resultados
        
            
   
    
def fracc(a,c,b): #Esta es la funcion fracc, sirve para imprimir la suma o resta de fracciones y regresar el resultado, para que posteriormente sea analizado
    if b==1: #checamos que dificultad es
            
        if a%2==0:#Vemos si va a ser suma o resta con el valor random
            
            x=ran.randrange(1,11)
            y=ran.randrange(1,11)
            z=ran.randrange(2,11)#Sacamos 3 variables random para identificar los numeros dentro de las fracciones
            print(str(c+1) +'- Suma esta fracción:\n'+str(x) + '   '+str(y) + '\n- + - =\n' + str(z) + '   ' + str(z))# Imprimimos para que se vea bien
            return (x+y)/z #Regresamos el resultado
        else:
            x=ran.randrange(1,11)
            y=ran.randrange(1,11)
            z=ran.randrange(2,11) #Lo mismo pero con una resta ahora
            print(str(c+1) +'- Resta esta fracción:\n'+str(x) + '   '+str(y) + '\n- - - =\n' + str(z) + '   ' + str(z))
            return (x-y)/z #Regresamos resultado pero ahora con resta
    elif b==2: #Repetimos lo mismo con otra dificultad
        if a%2==0:
            
            x=ran.randrange(1,11)
            y=ran.randrange(1,11)
            z=ran.randrange(2,11)
            z2=ran.randrange(2,11) #Ahora con mas variables aleatorias para mayor dificultad
            print(str(c+1) +'- Suma esta fracción:\n'+str(x) + '   '+str(y) + '\n- + - =\n' + str(z) + '   ' + str(z2))
            return (x+y)/z
        else:
            x=ran.randrange(1,11)
            y=ran.randrange(1,11)
            z=ran.randrange(2,11)
            z2=ran.randrange(2,11)#Ahora lo mismo pero en resta
            print(str(c+1) +'- Resta esta fracción:\n'+str(x) + '   '+str(y) + '\n- - - =\n' + str(z) + '   ' + str(z2))
            return (x/z)-(y/z2)
    elif b==3: # Lo mismo pero con numeros mas altos ahora y ya
        if a%2==0:
            
            x=ran.randrange(1,20)
            y=ran.randrange(1,20)
            z=ran.randrange(2,20)
            z2=ran.randrange(2,20)
            print(str(c+1) +'- Suma esta fracción:\n'+str(x) + '   '+str(y) + '\n- + - =\n' + str(z) + '   ' + str(z2))
            return (x+y)/z
        else:
            x=ran.randrange(1,20)
            y=ran.randrange(1,20)
            z=ran.randrange(2,20)
            z2=ran.randrange(2,20)
            print(str(c+1) +'- Resta esta fracción:\n'+str(x) + '   '+str(y) + '\n- - - =\n' + str(z) + '   ' + str(z2))
            return (x/z)-(y/z2)
    repetir_juego(fracc)

#_____________________________________ FIN SUMA Y RESTA FRACCIONES__________________________________

#_____________________________________PORCENTAJES__________________________________
def porcentajes(): #Iniciamos funcion que sera usada en el menu
    print('- - - Iniciando juego de porcentajes - - -\n')
    
    while True: #comenzamos con un while para determinar la longitud del jeugo
        puntuacion=0 #declaramos una variable que vamos a usar
        dificultad=int(input('¿Que nivel quieres 1, 2 o 3?'))
        if dificultad==1: #Checamos dificultad
            for r in range(5): #hacemos que se repita varias veces
                random=ran.randrange(10,90,10)
                numero=ran.randrange(100,1000,10) #sacamos dos numeros random determinador por su dificultad
                print('Cuanto es el ' + str(random) + '% de ' + str(numero) + ': ')
                respuesta=float(input('')) # imprimimos y preguntamos por el resultado
                if respuesta==(random/100)*numero:#confirmamos que sea correcto
                    puntuacion=puntuacion+1 #sumamos un punto
                    print('Correcto\n')#aprovacion
                else:
                    print('Incorrecto\n') #si no es correcto se lo mencionamos
            print(puntuacion,'/5') #imprimimos la puntuacion
            print('- - - Saliendo juego de porcentajes - - -\n')
            return ['Porcentajes dif 1', puntuacion] #mandamos una lista al menu para el hisotiral y la puntuacion
        elif dificultad==2: #Checamos dificultad y repetimos lo anterior
            for r in range(5):
                random=ran.randrange(1,100)
                numero=ran.randrange(100,1000,10)#cambiamos el tipo de valores random
                print('Cuanto es el ' + str(random) + '% de ' + str(numero) + ': ')
                respuesta=float(input(''))
                if respuesta==(random/100)*numero:
                    puntuacion=puntuacion+1
                    print('Correcto\n')
                else:
                    print('Incorrecto\n')
            print(puntuacion,'/5')
            print('- - - Saliendo juego de porcentajes - - -\n')
            return ['Porcentajes dif 2', puntuacion]
        elif dificultad==3: #Checamos dificultad y repetimos de nuevo
            for r in range(5):
                random=ran.randrange(10,90)
                numero=ran.randrange(100,1000) #Volvemos a cambiar valores random
                print('Cuanto es el ' + str(random) + '% de ' + str(numero) + ': ')
                respuesta=float(input(''))
                if respuesta==(random/100)*numero:
                    puntuacion=puntuacion+1
                    print('Correcto\n')
                else:
                    print('Incorrecto\n')
            print(puntuacion,'/5')
            print('- - - Saliendo juego de porcentajes - - -\n')
            return ['Porcentajes dif 3', puntuacion]
        else: 
            print('No existe ese nivel, regresando al menu')
            break
    repetir_juego(porcentajes)
#_____________________________________FIN PORCENTAJES__________________________________
  
#_____________________________________HISTORIAL_________________________________________

def historial_resultados(l): #declaramos la funcion del historial y los resultados
    x=[]
    total=0
    print('--------------------Bienvenido al historial/resultados-------------------\n')
    try:
        decision= int(input('\n¿Que deseas jugar? \n1- Historial\n2- Resultados\n3- Salir'))
        if decision==1: #preguntamos por la decision con base a eso usamos if's para llegar a su procedimiento
            print('\nEjercicio       Puntuación')
            for x in l:#Creamos un for para imprimir el historial, conforme a como se guardo
                if x[0]=='Encuentra el patron':
                    print(str(x[0]) + '     ' + str(x[1]) + ' veces equivocado')
                elif x[0]=='Ahorcado':#Pusimos algunos if's debido a que hay 3 ejercicios que no cumplen con la manera en la que la puntuacion se cuenta
                    print(str(x[0]) + '     ' + str(x[1]) + ' vidas restantes')
                elif x[0]=='Sopa de letras':
                    print(str(x[0]) + '     ' + str(x[1]) )
                        
                else:
                        
                    print(str(x[0])+ '    ' + str(x[1])) #Imprimimos todos los datos dentro de la lista
                    
                #total=total+x[1] #sumamos el total para imprimirlo al final de igual manera
            print('Puntuacion total: ', sum(puntaje))
        if decision==2: #Dentro de la decision 2 vamos a ver los resultados
            print('Resultados')
            lista_nombres=['Porcentajes dif 1','Porcentajes dif 2',
                           'Porcentajes dif 3','Suma y resta fracc dif 1',
                           'Suma y resta fracc dif 2','Suma y resta fracc dif 3',
                           'Suma y resta dif 1','Suma y resta dif 2',
                           'Suma y resta dif 3']
            #creamos una lista de los nombres de los ejercicios y sus puntuaciones
            lista_puntaje=[0,0,0, 0,0,0 ,0,0,0]#creamos una lista con los puntajes en 0 para despues substituirlos por los ya hechos
            lista_puntajet=[5,5,5, 5,5,5 ,9,9,25]#Creamos una lista con el total de los puntos por ejercicios
            
            for valor in l:
                for num in range(9): # Este for y el anterior es para encontrar si el puntaje ya obtenido es mayor al que esta y modificar la lista de puntajes, para posteriormente imprimirla
                    if valor[0]==lista_nombres[num] and valor[1]>lista_puntaje[num]:
                        lista_puntaje[num]=valor[1]
            for valor in range(9):#este for es para imprimir la lista de nombres junto con su puntaje actual y el total de dicho puntaje
            
                
                print(lista_nombres[valor], '       ', lista_puntaje[valor],'/',lista_puntajet[valor])
            print('\n')
    except ValueError: #Estos se encuentran por una buena parte del codigo, se trata de un try que impide que pongas algo que no sea un numero en momentos de eleccion, en plan cual eliges 1,2,3-
        print("La entrada de datos debe de ser numerica")
    
            
#_____________________________________FIN HISTORIAL_________________________________________

#_____________________________________SOPA DE LETRAS_________________________________________
def imprimirMatriz():#En esta funcion aplicamos dos ciclos while para ir imprimiendo la matriz primero renglon y luego por columna
      for z in range(len(matriz_letras)): 
        for a in range(len(matriz_letras[z])):
         print(matriz_letras[z][a], end=" ")
        print("     ",z,"\n")

abc= "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z" #Nuestro abecedario en string
abc_separado=abc.split() #Creamos un abc que nos sera de utilidad para la creacion de la matriz
bpalabras="MATEMATICAS CIENCIA KEPLER NEWTON SOL ASTROS SUMA RESTA DIVISION FRACCION REPETICION RAIZ CURIE BOHR ALGEBRA LECTURA APRENDER POTENCIA CUADRADO CUBO HIPOTENUSA PARMENIDES PITAGORAS TEOREMA ATOMO MOLECULA ELECTRON PROTON"
bpalabras_separado= bpalabras.split() #Separamos el banco de palabras en una lista
matriz_letras=[] #Aqui se agrgan las letras de manera aleatoria
max_renglon=len(max(bpalabras_separado, key=len)) #Variable que genera el maximo para los renglones dentro de la sopa de letras

def repetir_juego(modo):#Esta funcion tiene como objetivo el repetir un juego en caso de que algun jugador lo quiera volver a jugar, haciendo uso de parametros
    continuacion=str(input("Deseas seguir jugando este modo SI O NO = ")).lower()#Lo ponemos en .lower() porque es un a manera de evitar errores de dedo
    if(continuacion=="si"):
        modo()#Mandamos el parametro y agregamos parentesis para que se llame como funci
    else:
        print("LLAMAR MENU")

def generarMatriz(): #Esta funcion tiene como objetivo la creacion de una matriz con letras aleatorias y una altura y anchura determinadas
   for columnas in range(max_renglon*2):
        renglon=[]     #Esta variable son donde se iran acumulando todas las letras
        for renglones in range(max_renglon*2):
            renglon.append(abc_separado[rdm.randint(0, len(abc_separado)-1)]) #Aqui hacemos este codigo para que la sopa de letra se vaya generando con letras de nuestra lista
        matriz_letras.append(renglon) #Vamos agregando estos renglones de letras aleatorias
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
                puntaje.append(nvidas)
                return ['Sopa de letras', 'Ganaste']
                    
           
        else:
            nvidas=nvidas-1 #en caso de que no coincida restamos una vida 
            print("INCORRECTO,esa palabra no esta, VIDAS= ",nvidas)
        
            
            if(nvidas==0): #cuando el n de vidas es 0 es porque hemos perdido
                print("\n-------HAS PERDIDO-------\n")
                vivo=False #terminamos el ciclo while
                return ['Sopa de letras', 'Perdiste']
    if vivo==False:
        return ['Sopa de letras', 'Perdiste']
    if vivo==True:
        return ['Sopa de letras', 'Ganaste']

#_____________________________________FIN SOPA DE LETRAS_________________________________________

#_____________________________________AHORCADO_________________________________________
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
                print("\n-------Felicidades, es correcto la palabra era------- \n", palabra)
                vivo=False #En caso de generarla igualamos vivo a false para finalizar el ciclo while
                repetir_juego(ahorcado) 
                return ['Ahorcado',nvidas]#Damos este return para terminar con el juego
            
            for letra in range(len(palabra)): #Agui generamos este ciclo para que haga una comparacion letra con letra
                if intento==palabra or intento==palabra[letra]: 
                    renglon[letra]=intento #Vamos generando la lista con la palabra en base a la letra agragada
                    print("\nCORRECTO   VIDAS=", nvidas)
                    print(" ".join(renglon))
                if("".join(renglon)==palabra): #Aqui une la palabra para que sea un solo string y no una lista
                    print("-------Felicidades ganaste, es correcto la palabra era------- \n",palabra)
                    puntaje.append(nvidas)
                    vivo=False #Finalizamos ciclo while
        else:
            nvidas=nvidas-1 #Restamos una vida
            print("INCORRECTO    VIDAS=", nvidas)
            print(" ".join(renglon)) #imprimos el renglon sin cambios
            
            
            if(nvidas==0):
                print("\n-------HAS PERDIDO-------\n")
                vivo=False #finalizamos el juego porque se queddo sin vidas
    repetir_juego(ahorcado)
    return ['Ahorcado',nvidas] #Regresamos el nvidas como puntaje

#_____________________________________FIN AHORCADO_________________________________________

#_____________________________________EXCELL_________________________________________
def encontrar_patron(): #Esta funcion busca abrir el archivo excel, leerlo, imprirlo en orden y a partir de ahi generar una serie de preguntas 
    equivocado=0
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
        try:
            
            respuesta_usr=int(input("\nEncuentra el valor de x= "))#Aqui pedimos la respuesta del usuario 
        except ValueError:
            print("La entrada de datos debe de ser numerica")

        if(respuesta_usr==int(respuesta_incognita)): #Revisamos que la respuesta del usuario es la misma que la real
            aciertos=aciertos+1
            print("Respuesta correcta", aciertos,"puntos\n")
            if(aciertos==5): #Al momento de tener 5 aciertos seguidos finalizamos
                print("\nFelicidades tuviste 5 aciertos correctos seguidos! Ganaste")
                puntaje.append(aciertos)
                jugando=False
        else:
            print("\n Tenias", aciertos, "aciertos pero te equivocaste, asi que vuelves a empezar")
            equivocado=equivocado+1
            aciertos=0 #Igualamos a 0 el numero de aciertos porque tienen que tener 5 aciertos seguidos
    return ['Encuentra el patron', equivocado] 
#_____________________________________FIN EXCELL_________________________________________

def iniciar(l_f): #declaramos la funcion de iniciar los juegos
    
    while True: #Creamos un loop infinito hasta que quiera salir
        print('--------------------Bienvenido a la seccion de juegos-------------------\n')
        try:
            
            print('\n¿Que deseas jugar? \n1- Iniciar suma y resta\n2- Iniciar suma y resta de fracciones'+
                  '\n3-Iniciar Porcentajes \n4- Iniciar Ahorcado \n5- Iniciar Sopa de letras\n6- Encuentra el patron\n7- Salir')
            
            decision_iniciar=int(input('')) #preguntamos el juego que desea
            if decision_iniciar==1: #checamos decision con todos estos if's y mandamos a llamar la funcion deseada
                lista=suma_resta() #ademas de agregar los valores de los return dentro de la lista para el historial y los resultados
                #hicimos esto con todos los juegos
            if decision_iniciar==2:
                lista=sum_fracc()
                
            if decision_iniciar==3:
                lista=porcentajes()
                
            if decision_iniciar==4:
                lista=ahorcado()
                
            if decision_iniciar==5:
                lista=sopaletras()
                
            if decision_iniciar==6:
                lista=encontrar_patron()
            
            if decision_iniciar==7:
                print('--------------------Saliendo al menu-------------------\n')
                return l_f
            l_f.append(lista)
        except ValueError:
            print("La entrada de datos debe de ser numerica")
def menu(): #definimos el menu
    lista_final=[] #definimos nuesta lista_final, siendo importante para el conteo de las puntuaciones
    print('--------------------------------------------------\n' +
          '--------------------Bienvenido--------------------\n' +
          '--------------------------------------------------')
    while True: #iniciamos un loop infinito hasta que el usuario quiera salir
        try:
                
            print('\n¿Que deseas hacer? \n1- Iniciar\n2- Documentación\n3-Historial/Resultados\n4- Salir')
            decision_menu=int(input('')) #Preguntamos la decision del usuario
            if decision_menu==1: #checamos la decision del usuario
                lista_final=iniciar(lista_final) #mandamos a llamar funcion de iniciar los juegos
            elif decision_menu==2:#checamos la decision del usuario
                webbrowser.open("https://docs.google.com/document/d/1omBmYgMVkR9CYn6_XiRExGp8LRnfv3Xh-T0IlskF590/edit?usp=sharing")#mandamos a abrir nuestra documentacion
            elif decision_menu==3:#checamos la decision del usuario
                historial_resultados(lista_final)#mandamos a llamar la funcion de historial
            elif decision_menu==4:#checamos la decision del usuario
                print('--------------------------------------------------\n' +
                      '-----------Nos vemos, gracias por visitar---------\n' +
                      '--------------------------------------------------')
                break #salimos de todo
            else:
                print('opcion no valida')
        except ValueError:
            print("La entrada de datos debe de ser numerica")
menu()

