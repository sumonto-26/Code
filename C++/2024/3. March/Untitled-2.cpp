/*#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){

    double R;
    cin >> R;

    double x = (4.0/3);
    double formula = x * 3.14159 * pow(R,3);
    ans = "VOLUME = "<< fixed << setprecision(3) << formula <<endl;



    return 0;
}

#include <iostream>
using namespace std;

int main(){

    int a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;

    int ans = 0;

    if (a>b){
        if (a>c){
            ans = a ;
        }
        else{
            ans = c;
        }
    }

    else if (b>a){
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    else{
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    cout << ans << " eh o maior" << endl;

    return 0;
}


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

*/

// 1015 //
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    double x1,y1,x2,y2;
    cin >> x1;
    cin >> y1;
    cin >> x2;
    cin >> y2;

    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << fixed << setprecision(4) << distance << endl;

    return 0;
}