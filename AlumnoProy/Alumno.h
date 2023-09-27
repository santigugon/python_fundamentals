#ifndef ALUMNO_H_INCLUDED
#define ALUMNO_H_INCLUDED
#include <iostream>

using namespace std;

class Alumno {
    private:
        string matricula, nombre, carrera;
        int edad, jahre;

    public:
        void setMatricula(string);
        void setNombre(string);
        void setEdad(int);
        void setCarrera(string);

        string getMatricula();  //método get --> consulta valor de atributo
        string getNombre();
        int getEdad();
        string getCarrera();

        void imprimeAlumno();
        void cumpleanios();



};

#endif // ALUMNO_H_INCLUDED
