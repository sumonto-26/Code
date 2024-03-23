# include <iostream>
# include <iomanip>
using namespace std;

int main(){

    double a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;
    cout <<"NUMBER = " <<a << endl; 

    double ans = b*c;
    cout <<"SALARY = U$ "<< fixed << setprecision(2) << ans << endl;

    return 0;
}
