#include <iostream>


using namespace std;
#ifndef FRACCION_H_INCLUDED
#define FRACCION_H_INCLUDED

class Fraccion{
public:
Fraccion();
Fraccion(int, int);
~Fraccion();

int getDenominador();
int getNumerador();

void setDenominador(int);
void setNumerador(int);

double calcValorReal();
void imprimeFraccion();

private:
int denominador;
int numerador;

};

#endif