#include <iostream>
#include <string>
#include "Fraccion.h"

#ifndef CALCULADORA_H_INCLUDED
#define CALCULADORA_H_INCLUDED

using namespace std;

class Calculadora{
public:
void multiplicacion(Fraccion, Fraccion);
void division(Fraccion,Fraccion);

Fraccion getResultado();


private:
Fraccion operador1;
Fraccion operador2;
Fraccion resultado;

};




#endif