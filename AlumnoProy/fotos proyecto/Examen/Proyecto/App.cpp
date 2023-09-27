#include <iostream>
#include <string>
#include "C:\Users\santi\CPP-Proyectos\helloworld\Proyecto\Inventario.h"
#include "C:\Users\santi\CPP-Proyectos\helloworld\Proyecto\Medidas.h"
#include "C:\Users\santi\CPP-Proyectos\helloworld\Proyecto\Vestimenta.h"
#include "Cuenta.h"

using namespace std;

// Implementacion de inventario

// Constructores de inventario
Inventario::Inventario(){
unidades=0;
disponibilidad=false;
fechaAbastecimiento="N/a";
tipoInventario="N/A default";

}
Inventario::Inventario(int uds, bool disp, std::string fechaReab, std::string tipoInv){
unidades=uds;
disponibilidad=disp;
fechaAbastecimiento=fechaReab;
tipoInventario=tipoInv;
}


// getters de inventario
int Inventario::getUds(){
    return unidades;
}

bool Inventario::getDispo(){
    if (disponibilidad){
    cout<<"Esta disponible"<<endl;
    }else{
    cout<<"No esta disponible"<<endl;
    }
    return disponibilidad;
}

std::string Inventario::getFechaReab(){
    return fechaAbastecimiento;
}
std::string Inventario::getTipoInv(){
    return tipoInventario;
}

// Setters de Inventario

void Inventario::setUds(int uds){
    unidades=uds;
}

void Inventario::setDispo(bool dispo){
    disponibilidad=dispo;
}

void Inventario::setFechaReab(std::string fecha){
    fechaAbastecimiento=fecha;
}

void Inventario::setTipoInv(std::string tipo){
    tipoInventario=tipo;
}


// Metodos propios de inventario

void Inventario::reabastecer(){
    int numUds=Inventario::getUds();
    numUds+=100;
    Inventario::setUds(numUds);
}

void Inventario::imprimirInv(){
    int uds= Inventario::getUds();
    std::string tipoInv= Inventario::getTipoInv();
    std::string fecha= Inventario::getFechaReab();
    bool dispo= Inventario::getDispo();
    std::string textDispo;
    if (dispo){
    textDispo="esta disponible";
    cout<<"\n El producto si "<< textDispo<<" ya que cuenta con "<<uds<<"uds. Se trata de un inventario de tipo "<<tipoInv<<" que se reabastecera el "<<fechaAbastecimiento<<endl;
    }else{
    textDispo="no esta disponible";
    cout<<"El producto "<<textDispo<<" pero se reabastecera el "<<fecha<<endl;
    }

}


// Implementacion Medidas

// Constructores Vestimenta
Medidas::Medidas(){
 largo=0;
 ancho=0;
}
Medidas::Medidas(int lar, int anch){
largo=lar;
ancho=anch;
}
Medidas::Medidas(string tallaRe){
tallaRegular=tallaRe;
}
Medidas::Medidas(double numero){
calzado=numero;
}


// Implementacion Vestimenta

// Constructores Vestimenta
Vestimenta::Vestimenta(){
setUds(0);
setDispo(false);
setFechaReab("N/A");
color="N/A";
medidas= Medidas(0.0);
marca="Sin definir";
costo=0.0;
numVentas=0;
producto="N/A";
}


Vestimenta::Vestimenta(int uds, bool dispo, string reabastecimiento, string tipoInv, string col, Medidas tall, string temp, string mar, double costVent, int nVenta,string prod){
setUds(uds);
setDispo(dispo);
setFechaReab(reabastecimiento);
setTipoInv(tipoInv);
color=col;
medidas=tall;
marca=mar;
temporada=temp;
costo=costVent;
numVentas=nVenta;
producto=prod;
}
Vestimenta::Vestimenta(string col, Medidas tall, string temp, string mar, double costVent, int nVenta,string prod){
color=col;
medidas=tall;
marca=mar;
temporada=temp;
costo=costVent;
numVentas=nVenta;
producto=prod;
}

// getters de Vestimenta
string Vestimenta::getcolorUds(){
return color;
}
double Vestimenta::getCostoVenta(){
return costo;
}
string Vestimenta::getTemporada(){
return temporada;
}
int Vestimenta::getVentas(){
return numVentas;
}
string Vestimenta::getMarca(){
return marca;
}
string Vestimenta::getProducto(){
return producto;
}



// Setters de Vestimenta
void Vestimenta::setVentas(int vent){
numVentas=vent;
}
void Vestimenta::setColor(string col){
color= col;
}
void Vestimenta::setMedidas(Medidas talla){
medidas=talla;
}
void Vestimenta::setCosto(double cos){
costo=cos;
}
void Vestimenta::setMarca(string mar){
marca=mar;
}
void Vestimenta::setTemporada(string temp){
temporada= temp;
}
void Vestimenta::setProducto(string produ){
producto=produ;
}

// Metodos propios de vestimenta
void Vestimenta::agregarVenta(){
int ventas= this->getVentas();
this->setVentas(ventas++);

cout<<"\n Muchas gracias por tu compra!\n";
}
void Vestimenta::restarVenta(){
int ventas= this->getVentas();
this->setVentas(ventas--);
}
string Vestimenta::informeDevolucion(string razon, string producto, int uds){
cout<<"El producto "<<producto<<" se ha devuelto debido a "<<razon<<". Se devolvieron "<<uds<<"uds."<<endl;
return razon;
}
void Vestimenta::modificarProducto(string produ){
string colo;
string talla;
double tallaCalzado;
int medidaA;
int medidaB;
string temporad;
double costoVenta;
int ventas;
string product;
int unidade;
bool dispo;
string fechaReabastecimiento;
string tipoInventari;
string marc;

cout<<"\n---------------Bienvenido a la creacion de la instancia, porfavor ve paso a paso \n";
cout<<"Ingresa el color \n";
cin>>colo;
setColor(colo);


if(produ=="tenis"){
cout<<"Ingresa la talla en numeros decimales y, ej 7.5"<<endl;
cin>>tallaCalzado;
setMedidas(tallaCalzado);
}
else if(produ=="pantalones"){
cout<<"Ingresa la medida del alto de tus pantalones en enteros"<<endl;
cin>>medidaA;
cout<<"Ingresa la medida de ancho de tus pantalones en entero"<<endl;
cin>>medidaB;
setMedidas(Medidas(medidaA,medidaB));
}
else if(produ=="playeras"){
cout<<"Ingresa la talla de tu playera como largo, mediano o pequeño"<<endl;
cin>>talla;
setMedidas(talla);
}

cout<<"Ingresa la temporada"<<endl;
cin>>temporad;
setTemporada(temporad);

cout<<"Ingresa el costo al publico con decimales"<<endl;
cin>>costoVenta;
setCosto(costoVenta);

cout<<"Ingresa el numero de ventas"<<endl;
cin>>ventas;
setVentas(ventas);


cout<<"Ingresa el nombre del producto"<<endl;
cin>>product;
setProducto(product);

cout<<"Ingresa el numero de unidades en inventario"<<endl;
cin>>unidade;
setUds(unidade);


setDispo(true);


cout<<"Ingresa la proxima fecha de reabastecimiento"<<endl;
cin>>fechaReabastecimiento;
setFechaReab(fechaReabastecimiento);

cout<<"Ingresa el tipo de inventario"<<endl;
cin>>tipoInventari;
setTipoInv(tipoInventari);

cout<<"Ingresa la marca"<<endl;
cin>>marc;
setMarca(marc);


}

void Vestimenta::informeCompra(){

cout<<"Has comprado unos "<<producto<<" de la marca "<<marca<<" por un total de "<<costo;
}

// Destructor Vestimenta
Vestimenta::~Vestimenta(){
cout<<"Gracias por comprar con nosotros"<<endl;
}

//Implementacion Cuenta
Cuenta::Cuenta(){
nombre="John Doe";
usuario="JD";
contrasenia=0;
anioNacimiento=0;
}

Cuenta::Cuenta(string nom, int contra, int anio, string usu,bool perm){
nombre=nom;
contrasenia=contra;
anioNacimiento=anio;
usuario=usu;
permisos=perm;
}


// Getters
string Cuenta::getNombre(){
return nombre;
}

string Cuenta::getUsuario(){
return usuario;
}

int Cuenta::getAnioNacimiento(){
return anioNacimiento;
}

int Cuenta::getContrasenia(){
return contrasenia;
}


// Setters
void Cuenta::setNombre(string nom){
nombre= nom;
}

void Cuenta::setUsuario(string usu){
usuario=usu;
}

void Cuenta::setAnioNacimiento(int anio){
anioNacimiento=anio;
}

void Cuenta::setContrasenia(int contra){
contrasenia=contra;
}

// Metodos propios
void Cuenta::olvidoContrasenia(string usu, int anio){
string inputUsu=usu;
int inputAnio=anio;
if((inputUsu==usuario) && (inputAnio==anioNacimiento)){

}
}
void Cuenta::imprimirUsuario(){
cout<<"Nombre: "<<getNombre()<<"\nAño de Nacimiento: "<<anioNacimiento<<"\n Usuario: "<<usuario<<endl<<"Permisos:"<<permisos<< endl;
}

bool tenisB=false;
bool pantalonesB=false;
bool playerasB=false;
bool app=true;
// Funciones

Vestimenta Tenis;
Vestimenta Pantalones;
Vestimenta Playeras;

string menu="\n\nBienvenido al sistema de Ropa a tu gusto. \nPorfavor ingresa la accion que deseas realizar \n1)Ingresar como Administrador \n2)Ingresar como comprador ";
string menuUsuario="Bienvenido usuario \n 1)Crear cuenta\n2)Ingresar a cuenta\n 3)Regresar al menu\n";

bool cuenta=false;





void manejoInventario(bool tipoUsuario){
int inputUsuario;

if(tipoUsuario){
cout<<"\n\nBienvenido al manejo del inventario \n"<<"1)Crear Instancia\n"<<"2)Revisar Inventario actual\n 3)Modificar Inventario \n 4)Salir al menu princiapl"<<endl;
cin>>inputUsuario;


if(inputUsuario==1){
cout<<"\n Crear instancia de:\n1)Tenis \n2)Playeras \n3)Pantalones"<<endl;
inputUsuario=0;
cin>>inputUsuario;

if((inputUsuario==1)&&(!tenisB)){

Tenis.modificarProducto("tenis");
tenisB=true;

}else if(tenisB){
cout<<"Ya existe una instancia de Tenis"<<endl;
};

if((inputUsuario==2)&&(!playerasB)){
Playeras.modificarProducto("playeras");
playerasB=true;

}else if(playerasB){
cout<<"Ya existe una instancia de playeras"<<endl;
};
if((inputUsuario==3)&&(!pantalonesB)){
Pantalones.modificarProducto("pantalones");
pantalonesB=true;


}else if(pantalonesB){
cout<<"Ya existe una instancia de pantalones"<<endl;
};



}

else if(inputUsuario==2){
cout<<"Revisar inventario de:\n1)Tenis \n2)Pantalones \n3)Playeras"<<endl;
cin>>inputUsuario;
if((inputUsuario==1)&&(tenisB)){
Tenis.imprimirInv();

}else if(!tenisB){
cout<<"Primero crea una instancia de Tenis"<<endl;
};

if((inputUsuario==2)&&(playerasB)){
Playeras.imprimirInv();
}else if(!playerasB){
cout<<"\nPrimero crea una instancia de playeras"<<endl;
};
if((inputUsuario==3)&&(pantalonesB)){
Pantalones.imprimirInv();
}else if(!pantalonesB){
cout<<"\nPrimero crea una instancia de pantalones"<<endl;
};
}

else if(inputUsuario==3){
cout<<"\nModificar inventario de:\n1)Tenis \n2)Pantalones \n3)Playeras"<<endl;
inputUsuario=0;
cin>>inputUsuario;

if((inputUsuario==1)&&(tenisB)){

Tenis.modificarProducto("tenis");


}else if(!tenisB){
cout<<"No existe una instancia de Tenis"<<endl;
};

if((inputUsuario==2)&&(playerasB)){
Playeras.modificarProducto("playeras");


}else if(!playerasB){
cout<<"No existe una instancia de playeras"<<endl;
};
if((inputUsuario==3)&&(pantalonesB)){
Pantalones.modificarProducto("pantalones");



}else if(!pantalonesB){
cout<<"No existe una instancia de playeras"<<endl;
};



}

else if(inputUsuario==4){
return;
}


if((inputUsuario>4)&&(inputUsuario<1)){
cout<<"Ingresa un numero valido entre 1 y 4"<<endl;
}
manejoInventario(true);

}

else if(!tipoUsuario){
inputUsuario=0;
cout<<"\nBienvenido a la tienda de ropa TU MEJOR COMPRA\n"<<"1)Comprar un producto\n"<<"2)Devolver un producto\n 3)Ver disponibilidad de un producto \n 4)Salir al menu princiapl"<<endl;
cin>>inputUsuario;


if(inputUsuario==1){
cout<<"Comprar:\n1)Tenis \n2)Pantalones \n3)Playeras"<<endl;
inputUsuario=0;
cin>>inputUsuario;

if(inputUsuario==1){

Tenis.agregarVenta();
Tenis.informeCompra();

}

if((inputUsuario==2)){
Playeras.agregarVenta();
Playeras.informeCompra();

}
if((inputUsuario==3)){
Pantalones.agregarVenta();
Pantalones.informeCompra();


}



}

else if(inputUsuario==2){
inputUsuario=0;
cout<<"Devolver:\n1)Tenis \n2)Pantalones \n3)Playeras"<<endl;

cin>>inputUsuario;

int uds;
cout<<"Indica el numero de uds que vas a devolver porfavor"<<endl;
cin>>uds;


string razon;
cout<<"Tuviste problemas de calidad con el producto(si o no) "<<endl;
cin>>razon;


if((inputUsuario==1)){

Tenis.informeDevolucion(razon,"Tenis",uds);

}

if((inputUsuario==2)){
Pantalones.informeDevolucion(razon,"Pantalon(es)",uds);
};
if((inputUsuario==3)){
Playeras.informeDevolucion(razon,"Playera(s)",uds);

};
inputUsuario=0;
}

else if(inputUsuario==3){
cout<<"Ver disponibilidad de:\n1)Tenis \n2)Pantalones \n3)Playeras"<<endl;
inputUsuario=0;
cin>>inputUsuario;

if((inputUsuario==1)&&(tenisB)){

Tenis.getDispo();


}else if(!tenisB){
cout<<"No existe una instancia de Tenis"<<endl;
};

if((inputUsuario==2)&&(playerasB)){
Playeras.getDispo();


}else if(!playerasB){
cout<<"No existe una instancia de playeras"<<endl;
};
if((inputUsuario==3)&&(pantalonesB)){
Pantalones.getDispo();
};



}

else if(inputUsuario==4){

return;
}


if((inputUsuario>4)&&(inputUsuario<1)){
cout<<"Ingresa un numero valido entre 1 y 4"<<endl;
}
manejoInventario(false);


}

}

void App(){

int decision=0;
int decisionUsu=0;

cout<<menu<<endl;
cin>>decision;
if(decision==1){
cout<<menuUsuario;
cin>>decisionUsu;


if(decisionUsu==1){
string usuario;
string nombre;
int anioNacimiento;
int contrasenia;
bool permisos=true;

cout<<"Ingresa tu nombre de usuario: \n";
cin>>usuario;

cout<<"Ingresa tu nombre: \n";
cin>>nombre;

cout<<"Ingresa tu contraseña: \n";
cin>>contrasenia;

cout<<"Ingresa tu año de nacimiento: \n";
cin>>anioNacimiento;

Cuenta instanciaCuenta(nombre, contrasenia, anioNacimiento,usuario,permisos);
cuenta=true;
instanciaCuenta.imprimirUsuario();
manejoInventario(true);
}

if(decisionUsu==2){
if(!cuenta){
cout<<"Primero crea una cuenta "<<endl;
return;
}
string nombre;
cout<<"\n Ingresa tu usuario"<<endl;
cin>>nombre;

int contra;
cout<<"\n Ingresa la contraseña"<<endl;

cout<<"\nBienvenido a tu cuenta!\n";
manejoInventario(true);
}

else if(decisionUsu==3){
return;
}

}else if(decision==2){

manejoInventario(false);

}

else{
cout<<"Ingresa una opcion valida porfavor";
}



}

// APLICACION
int main(){

while(app){
App();
}
// while (app){
// app=false;
// int decision=0;
// int decisionUsu=0;

// cout<<menu<<endl;
// cin>>decision;
// if(decision==1){
// cout<<menuUsuario;
// cin>>decisionUsu;


// if(decisionUsu==1){
// string usuario;
// string nombre;
// int anioNacimiento;
// int contrasenia;
// bool permisos=true;

// cout<<"Ingresa tu nombre de usuario: \n";
// cin>>usuario;

// cout<<"Ingresa tu nombre: \n";
// cin>>nombre;

// cout<<"Ingresa tu contraseña: \n";
// cin>>contrasenia;

// cout<<"Ingresa tu año de nacimiento: \n";
// cin>>anioNacimiento;

// Cuenta instanciaCuenta(nombre, contrasenia, anioNacimiento,usuario,permisos);
// cuenta=true;
// instanciaCuenta.imprimirUsuario();

// if(decisionUsu==2){
// if(!cuenta){
// cout<<"Primero crea una cuenta "<<endl;
// break;
// }
// string nombre;
// cout<<"\n Ingresa tu usuario"<<endl;
// cin>>nombre;

// int contra;
// cout<<"\n Ingresa la contraseña"<<endl;

// cout<<"Bienvenido a tu cuenta!";
// manejoInventario(true);
// }
// }
// }else if(decision==2){
// app=false;
// manejoInventario(false);

// }
// else{
// cout<<"Ingresa una opcion valida porfavor";
// }


// }



// playera.imprimirInv();
// cout<<playera.getUds()<<endl;
// Vestimenta prueba;
// cout<<prueba.getTipoInv()<<endl;
return 0;
}