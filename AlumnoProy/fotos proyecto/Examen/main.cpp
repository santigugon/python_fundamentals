#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cctype>
#include <ctime>
#include "Fraccion.h"
#include "Calculadora.h"
#include "Impropia.h"

using namespace std;
// Implementacion de Fraccion
Fraccion::Fraccion(){
numerador=1;
denominador=2.0;
}
Fraccion::Fraccion(int num,int den){
numerador=num;
denominador=den;
}
Fraccion::~Fraccion(){}

// Getters Fraccion
int Fraccion::getDenominador(){
return denominador;
}
int Fraccion::getNumerador(){
return numerador;
}

// Setters Fraccion

void Fraccion::setDenominador(int den){
denominador=den;
}
void Fraccion::setNumerador(int num){
numerador=num;
}

// Metodos propios
double Fraccion::calcValorReal(){
double valorReal=((double)numerador/denominador);
cout<<"\nEl valor real es de "<<valorReal<<endl;
return valorReal;

}

void Fraccion::imprimeFraccion(){

cout<<(double)numerador<<"/"<<denominador;
}

// Implementacion Calculadora

// Metodos propios Calculadora
Fraccion Calculadora::getResultado(){
return resultado;
}


void Calculadora::multiplicacion(Fraccion frac1, Fraccion frac2){
int numUno=frac1.getNumerador();
int numDos=frac2.getNumerador();
int den1=frac1.getDenominador();
int den2=frac2.getDenominador();

cout<<"\nEl resultado de la multiplicacion ";
frac1.imprimeFraccion();
cout<<" X ";
frac2.imprimeFraccion();
cout<<"="<<endl;
int resultadoNum=numUno*numDos;
int resultadoDen=den1*den2;
resultado=Fraccion(resultadoNum,resultadoDen);
resultado.imprimeFraccion();
resultado.calcValorReal();
cout<<"-----------------------------"<<endl;
}

void Calculadora::division(Fraccion frac1, Fraccion frac2){
int numUno=frac1.getNumerador();
int numDos=frac2.getNumerador();
int den1=frac1.getDenominador();
int den2=frac2.getDenominador();

cout<<"\nEl resultado de la division ";
frac1.imprimeFraccion();
cout<<" / ";
frac2.imprimeFraccion();
cout<<"="<<endl;
int resultadoNum=numUno*den2;
int resultadoDen=den1*numDos;
resultado=Fraccion(resultadoNum,resultadoDen);
resultado.imprimeFraccion();
resultado.calcValorReal();
cout<<"-----------------------------"<<endl;
}

// Implementacion impropia
// Constructores y destructores
Impropia::Impropia(){
setNumerador(1);
setDenominador(2);
setEntero(1);
}
Impropia::Impropia(int num, int den){
setNumerador(num);
setDenominador(den);
entero=0;
}
Impropia::~Impropia(){
cout<<"\nGracias por tu participacion en la materia TC1033";
}
// Getters y setters
void Impropia::setEntero(int ent){
entero=ent;
}
int Impropia::getEntero(){
return entero;
}

void Impropia::representa(){
int num=getNumerador();
int den=getDenominador();
if(num>den){
imprimeFraccion();
entero=getNumerador()/getDenominador();
setNumerador(num-(entero*den));


cout<<"\nLa fraccion con su entero es= "<<entero<<"  ";
imprimeFraccion();
}else{
imprimeFraccion();
}



}

void Impropia::validaImpropia(){
int num=getNumerador();
int den=getDenominador();
if(num>den){
cout<<endl<<"\nLa fraccion SI es impropia \n";
}else{
cout<<"\nLa fraccion NO es impropia \n";
}
}




int main(){

Fraccion cargada2(2,3);


Fraccion cargada(1.0,4);

Calculadora basica;

basica.multiplicacion(cargada,cargada2);
basica.division(cargada, cargada2);

Fraccion resultado=basica.getResultado();


cout<<"\n \nFraccion impropia\n";
Impropia prueba(5,2);

prueba.validaImpropia();
prueba.representa();

// prueba.calcValorReal();
// prueba.imprimeFraccion();

// cargada.calcValorReal();
// cargada.imprimeFraccion();

return 0;

}