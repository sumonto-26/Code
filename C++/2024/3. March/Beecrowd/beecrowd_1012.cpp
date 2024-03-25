
#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    double a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;


    double TRIANGULO = (a*c)/2;
    cout << "TRIANGULO: " << fixed << setprecision(3) << TRIANGULO <<endl;

    double CIRCULO = 3.14159*c*c;
    cout << "CIRCULO: " << fixed << setprecision(3) << CIRCULO <<endl;

    double TRAPEZIO = ((a+b)/2)*c;
    cout << "TRAPEZIO: " << fixed << setprecision(3) << TRAPEZIO <<endl;

    double QUADRADO = b*b;
    cout << "QUADRADO: " << fixed << setprecision(3) << QUADRADO <<endl;

    double RETANGULO = a*b;
    cout << "RETANGULO: " << fixed << setprecision(3) << RETANGULO <<endl;


    return 0;
}