#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    string costomer;
    cin >> costomer;

    double a,b;
    cin >> a;
    cin >> b;
 
    double ans = (a + ((b/100)*15));

    cout <<"TOTAL = R$ "<< fixed << setprecision(2) << ans << endl;


    return 0;
}