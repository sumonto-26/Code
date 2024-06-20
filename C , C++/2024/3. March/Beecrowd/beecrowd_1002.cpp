#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){

    double x;
    cin >> x;

    double ans = 3.14159 * (x * x);

    cout << "A=" << fixed << setprecision(4) << ans << endl;

    return 0;
}