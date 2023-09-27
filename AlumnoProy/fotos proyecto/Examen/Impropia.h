#include <iostream>
#include "Fraccion.h"

using namespace std;
#ifndef IMPROPIA_H_INCLUDED
#define IMPROPIA_H_Impropia

class Impropia:public Fraccion{
public:
Impropia();
Impropia(int, int);

int getEntero();
void setEntero(int);

~Impropia();

void validaImpropia();
void representa();

private:
int entero;
};
#endif