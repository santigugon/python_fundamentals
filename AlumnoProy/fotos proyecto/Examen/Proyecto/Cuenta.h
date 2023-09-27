#include <iostream>
#include <string>
#include "Inventario.h"
#include "Medidas.h"

using namespace std;

class Cuenta{

public:

// Constructor
Cuenta();
Cuenta(string,int,int,string,bool);

// Getters
string getNombre();
string getUsuario();
int getContrasenia();
int getAnioNacimiento();
bool getPermisos();

// Setters
void setNombre(string nom);
void setUsuario(string usu);
void setContrasenia(int contra);
void setAnioNacimiento(int anio);

// Metodos Especiales
void olvidoContrasenia(string usu, int anio);
void imprimirUsuario();

private:

string usuario;
int contrasenia;
int anioNacimiento;
bool permisos;
string nombre;



};