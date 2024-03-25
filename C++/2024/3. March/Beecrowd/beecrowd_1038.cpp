#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    float menu[5] = {4.00, 4.50, 5.00, 2.00, 1.50};
    
    int a; cin >> a;
    int b; cin >> b;


    cout << "Total: R$ " << fixed << setprecision(2) << menu[a-1]*b << endl;


    return 0;
}