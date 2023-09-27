#include <iostream>
#include <string>
#include "Inventario.h"
#include "Medidas.h"

using namespace std;

#ifndef VESTIMENTA_H_INCLUDED
#define VESTIMENTA_H_INCLUDED


class Vestimenta: public Inventario{
public:
Vestimenta();
Vestimenta(int uds, bool dispo, string reabastecimiento, string tipoInv, string color, Medidas talla, string temporada, string marca, double costoVenta, int numVentas,string prod);
Vestimenta(string col, Medidas tall, string temp, string mar, double costVent, int nVenta,string prod);

void informeCompra();
void agregarVenta();
void restarVenta();
string informeDevolucion(string, string, int);
void modificarProducto(string);


int getVentas();
double getCostoVenta();
string getcolorUds();
string getTemporada();
string getMarca();
string getProducto();



void setVentas(int);
void setColor(string);
void setMedidas(Medidas);
void setCosto(double);
void setMarca(string);
void setProducto(string);
void setTemporada(string);

~Vestimenta();


private:
string color;
Medidas medidas;
string marca;
string temporada;
double costo;
int numVentas;
string producto;


};
#endif