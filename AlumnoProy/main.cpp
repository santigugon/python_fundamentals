#include <iostream>
#include "Alumno.h"

using namespace std;

int main()
{
    string a, b, d;
    int c;

    cout<<"Ingresa tu matricula: "<<"\n";
    cin>>a;
    cout<<"Ingresa tu nombre: "<<"\n";
    cin>>b;
    cout<<"Ingresa tu carrera: "<<"\n";
    cin>>d;
    cout<<"Ingresa tu edad: "<<"\n";
    cin>>c;


    Alumno almn;

    almn.setMatricula(a);
    almn.setNombre(b);
    almn.setEdad(c);
    almn.setCarrera(d);

    almn.imprimeAlumno();
    almn.cumpleanios();

    return 0;
}
