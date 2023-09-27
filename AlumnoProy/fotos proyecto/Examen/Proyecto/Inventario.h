


#include <iostream>
#include <string>

using namespace std;

#ifndef INVENTARIO_H_INCLUDED
#define INVENTARIO_H_INCLUDED


class Inventario{
public:
//Constructores
Inventario();
Inventario(int uds, bool disp, string fechaReab, string tipoInv);

//Metodos
int getUds();
bool getDispo();
string getFechaReab();
string getTipoInv();

void setUds(int);
void setDispo(bool);
void setFechaReab(string);
void setTipoInv(string);


void reabastecer();
void imprimirInv();


private:
int unidades;
bool disponibilidad;
string fechaAbastecimiento;
string tipoInventario;

};
#endif