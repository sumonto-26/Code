#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    
    double a;
    cin >> a;
    double b;
    cin >> b;
    double c;
    cin >> c;


    double answer = ((a*2)+(b*3)+(c*5))/10;
    cout << "MEDIA = " << fixed << setprecision(1) << answer << endl;
   
    return 0;
}