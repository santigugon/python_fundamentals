#include <iostream>
#include <string>

using namespace std;

#ifndef MEDIDAS_H_INCLUDED
#define MEDIDAS_H_INCLUDED


class Medidas{
public:
Medidas();
Medidas(int,int);
Medidas(double);
Medidas(string);



private:
int largo;
int ancho;
double calzado;
string tallaRegular;

};
#endif