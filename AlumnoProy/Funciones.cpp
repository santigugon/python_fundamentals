#include <iostream>
#include "Alumno.h"

using namespace std;

string Alumno::getMatricula(){
            return matricula;
            }

string Alumno::getNombre(){
            return nombre;
            }

string Alumno::getCarrera(){
            return carrera;
            }

int Alumno::getEdad(){
            return edad;
            }

void Alumno::setMatricula(string mat){
            matricula = mat;
            }

void Alumno::setNombre(string nom){
            nombre = nom;
            }

void Alumno::setEdad(int age){
            edad = age;
            }

void Alumno::setCarrera(string car){
            carrera = car;
            }

void Alumno::imprimeAlumno(){
            cout<<"\nNombre: "<<nombre<<endl;
            cout<<"Matricula: "<<matricula<<endl;
            cout<<"Edad: "<<edad<<endl;
            cout<<"Carrera: "<<carrera<<endl;
            }
void Alumno::cumpleanios(){
            jahre = edad+1;
            cout<<"\nCumpleanios: "<<jahre<<endl;

            }
