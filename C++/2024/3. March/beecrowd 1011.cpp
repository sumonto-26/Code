#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){

    double R;
    cin >> R;

    double x = (4.0/3);
    double formula = x * 3.14159 * pow(R,3);
    cout << "VOLUME = "<< fixed << setprecision(3) << formula <<endl;



    return 0;
}