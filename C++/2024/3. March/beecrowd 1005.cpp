#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    
    double a;
    cin >> a;
    double b;
    cin >> b;


    double answer = ((a*3.5)+(b*7.5))/11;
    cout << "MEDIA = " << fixed << setprecision(5) << answer << endl;
   
    return 0;
}